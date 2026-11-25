"""Render website pages and resource files from typed lab content."""

import re
from dataclasses import dataclass
from datetime import date
from html import escape, unescape
from pathlib import Path
from string import Template
from urllib.parse import urlsplit

from site_content import (
    Highlight,
    HighlightPaper,
    HighlightPerson,
    HighlightResource,
    HighlightTutorial,
    NewsItem,
    Paper,
    SearchRecord,
    SiteContent,
)

SITE_ORIGIN = "https://westlake-encode-lab.github.io"
PAGE_ROUTES = {
    "Home": "",
    "People": "people/",
    "Publications": "publications/",
    "News": "news/",
    "Talks": "talks/",
    "Gallery": "gallery/",
}
SITE_DESCRIPTION = "Efficient Neural Computing and Design at Westlake University."
SOCIAL_ICONS = {
    "Homepage": "house",
    "Email": "envelope",
    "Google Scholar": "google-scholar",
    "GitHub": "github",
    "LinkedIn": "linkedin",
    "X": "x-twitter",
}
SOCIAL_ORDER = {label: index for index, label in enumerate(SOCIAL_ICONS)}
VENUE_CATEGORIES = {
    "CVPR": "vision",
    "ICCV": "vision",
    "ECCV": "vision",
    "ICML": "learning",
    "ICLR": "learning",
    "NeurIPS": "learning",
    "arXiv": "preprint",
}

@dataclass(frozen=True)
class RenderedSite:
    pages: dict[str, str]
    search_records: list[SearchRecord]
    bibliography: str

class SiteRenderer:
    def __init__(self, root: Path, content: SiteContent, updated: date) -> None:
        self._root: Path = root
        self._content: SiteContent = content
        self._updated: date = updated
        self._base_template: Template = Template((root / "templates/base.html").read_text(encoding="utf-8"))
        self._home_template: Template = Template((root / "templates/home.html").read_text(encoding="utf-8"))
        self._highlight_template: Template = Template((root / "templates/highlight.html").read_text(encoding="utf-8"))
        self._icons: dict[str, str] = {}
        self._pages: dict[str, str] = {}
        self._search_records: list[SearchRecord] = []
        for path in sorted((root / "assets/icons").glob("*.svg")):
            self._icons[path.stem] = (
                path.read_text(encoding="utf-8")
                .strip()
                .replace(
                    "<svg ",
                    '<svg class="link-icon" aria-hidden="true" focusable="false" fill="currentColor" ',
                    1,
                )
            )

    def render_site(self) -> RenderedSite:
        self._pages.clear()
        self._search_records.clear()
        papers = self._content.papers
        authors = self._content.authors
        news = sorted(self._content.news, key=lambda item: item["date"], reverse=True)
        for name, directory in PAGE_ROUTES.items():
            self._add_search_record("Page", name, f"{directory}index.html")
        self._add_search_record("Contact", "Email ENCODE Lab", "mailto:encodelab@westlake.edu.cn")
        self._add_search_record("Contact", "ENCODE Lab on GitHub", "https://github.com/westlake-encode-lab")
        self._add_search_record(
            "Admissions",
            "Admission guide (PDF)",
            "assets/pdf/admission.pdf",
            "join PhD postdoc openings visiting students",
        )
        for item in news:
            self._add_news_page(item)

        bodies = {
            "Home": self._home_page(news),
            "People": self._people_page(),
            "Talks": self._talks_page(),
            "Publications": self._publications_page(papers, authors),
            "News": self._news_page(news),
            "Gallery": self._gallery_page(),
        }
        for name, body in bodies.items():
            self._add_page(f"{PAGE_ROUTES[name]}index.html", name, name, body)
        for highlight in self._content.highlights:
            self._add_highlight_page(highlight)
        self._add_page(
            "404.html",
            "",
            "Page not found",
            _heading("Page not found") + '<p class="story"><a href="@/index.html">Return to the homepage</a></p>',
        )
        bibliography = "\n\n".join(_bibliography(paper) for paper in papers) + "\n"
        return RenderedSite(self._pages.copy(), self._search_records.copy(), bibliography)

    def _add_page(
        self,
        path: str,
        section: str,
        title: str,
        body: str,
        description: str = SITE_DESCRIPTION,
        *,
        stylesheet: str = "",
        share_image: str = "assets/img/lab.jpg",
    ) -> None:
        # GitHub Pages serves the 404 page at arbitrary path depths.
        root = "/" if path == "404.html" else ("../" * path.count("/") or "./")
        canonical = f"{SITE_ORIGIN}/{path.removesuffix('index.html')}"
        navigation = []
        for name, directory in PAGE_ROUTES.items():
            active = ' aria-current="page"' if section == name else ""
            navigation.append(f'<a href="@/{directory}index.html"{active}>{name}</a>')
        footer_contacts = self._icon_link(
            "https://github.com/westlake-encode-lab", "GitHub", "github", icon_only=True
        ) + self._icon_link("mailto:encodelab@westlake.edu.cn", "encodelab@westlake.edu.cn", "envelope")
        document = self._base_template.substitute(
            title=escape("Westlake ENCODE Lab" if section == "Home" else f"{title} · Westlake ENCODE Lab"),
            description=escape(description),
            footer_contacts=footer_contacts,
            canonical=canonical,
            root=root,
            updated=self._updated.isoformat(),
            nav="\n".join(navigation),
            body=body,
            extra_styles=f'<link rel="stylesheet" href="@/{escape(stylesheet)}">' if stylesheet else "",
            share_image=f"{SITE_ORIGIN}/{escape(share_image)}",
        )
        self._pages[path] = document.replace("@/", root)

    def _add_highlight_page(self, highlight: Highlight) -> None:
        event = f"{highlight['venue']} {highlight['year']}"
        people = "".join(self._highlight_person(person) for person in highlight["people"])
        tutorial = highlight.get("tutorial")
        tutorial_nav = '<a href="#tutorial">Tutorial</a>' if tutorial else ""
        if "host" in highlight:
            event_detail = self._highlight_person(highlight["host"])
        else:
            tutorial_count = '<span><strong>1</strong> tutorial</span>' if tutorial else ""
            event_detail = (
                f'<div class="highlight-counts"><span><strong>{len(highlight["papers"])}</strong> papers</span>'
                f'{tutorial_count}</div>'
            )
        people_section = (
            '<section class="highlight-section" id="contributors"><div class="highlight-section-heading">'
            f'<p class="eyebrow">{escape(highlight["people_kicker"])}</p>'
            f'<h2>{escape(highlight["people_title"])}</h2><p>{escape(highlight["people_intro"])}</p></div>'
            f'<div class="highlight-people">{people}</div></section>'
        ) if people else ""
        tags = "".join(f"<li>{escape(tag)}</li>" for tag in highlight["tags"])
        keywords = " · ".join(map(escape, highlight["keywords"]))
        category = VENUE_CATEGORIES.get(highlight["venue"], "other")
        body = self._highlight_template.substitute(
            event=escape(event),
            category=category,
            eyebrow=escape(highlight["eyebrow"]),
            headline=highlight["headline_html"],
            introduction=highlight["introduction_html"],
            tags=f'<ul class="highlight-tags">{tags}</ul>' if tags else "",
            keywords=f'<p class="highlight-keywords">{keywords}</p>' if keywords else "",
            event_detail=event_detail,
            image=escape(highlight["image"]),
            image_width=highlight["image_width"],
            image_height=highlight["image_height"],
            image_alt=escape(highlight["image_alt"]),
            image_credit=highlight["image_credit"],
            papers_heading=escape(highlight["papers_heading"]),
            paper_layout="illustrated" if any("image" in feature for feature in highlight["papers"]) else "text",
            papers="".join(self._highlight_paper(feature) for feature in highlight["papers"]),
            tutorial=self._highlight_tutorial(tutorial) if tutorial else "",
            tutorial_nav=tutorial_nav,
            people_nav='<a href="#contributors">People</a>' if people else "",
            people=people_section,
        )
        path = f"highlights/{highlight['id']}/index.html"
        title = f"{event} highlights"
        self._add_page(
            path, "", title, body, _plain_text(highlight["introduction_html"]),
            stylesheet="assets/highlights.css", share_image=highlight["image"],
        )
        keywords = " ".join(feature["title"] for feature in highlight["papers"])
        self._add_search_record("Highlights", title, path, keywords)

    def _highlight_paper(self, feature: HighlightPaper) -> str:
        session = f'<p class="highlight-session">{escape(feature["session"])}</p>' if "session" in feature else ""
        summary = f'<p class="highlight-summary">{feature["summary_html"]}</p>' if "summary_html" in feature else ""
        figure = ""
        if "image" in feature:
            source = f"@/{escape(feature['image'])}"
            caption = ""
            if "image_caption" in feature:
                caption = f'<figcaption>{escape(feature["image_caption"])}</figcaption>'
            figure = (
                f'<figure><a href="{source}" aria-label="Open research figure for {escape(feature["title"])}">'
                f'<img src="{source}" alt="{escape(feature.get("image_alt", ""))}" loading="lazy"></a>'
                f"{caption}</figure>"
            )
        resources = " ".join(self._highlight_resource(resource) for resource in feature["resources"])
        return (
            '<section class="highlight-paper">'
            f'<article class="paper" id="{feature["paper_id"]}"><h3>{escape(feature["title"])}</h3>'
            f'<p class="highlight-topic">{escape(feature["topic"])}</p>{session}{summary}'
            f'<p class="authors">{feature["authors_html"]}</p><div class="links">{resources}</div></article>'
            f"{figure}</section>"
        )

    def _highlight_resource(self, resource: HighlightResource) -> str:
        label = resource["label"]
        if "url" not in resource:
            return f'<span class="resource-status">{escape(label)}</span>'
        icon = {"arxiv": "arxiv", "pdf": "file-pdf", "code": "github"}.get(label.lower(), "globe")
        return self._icon_link(resource["url"], label, icon)

    def _highlight_person(self, person: HighlightPerson) -> str:
        role = f'<p class="highlight-role">{escape(person["role"])}</p>' if "role" in person else ""
        return (
            f'<a class="highlight-person" href="{escape(person["url"])}"><span class="portrait">'
            f'<img src="@/{escape(person["photo"])}" alt="" width="128" height="160" loading="lazy"></span>'
            f'<div><strong>{escape(person["name"])}</strong><p>{escape(person["contribution"])}</p>{role}</div></a>'
        )

    def _highlight_tutorial(self, tutorial: HighlightTutorial) -> str:
        topics = "".join(
            f'<li><h3>{escape(topic["title"])}</h3><p>{escape(topic["summary"])}</p></li>'
            for topic in tutorial["topics"]
        )
        facts = "".join(
            f"<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>"
            for label, value in tutorial["facts"].items()
        )
        schedule = "".join(
            f'<li><time>{escape(session["time"])}</time><div><strong>{escape(session["title"])}</strong>'
            f'<p>{escape(session["speaker"])}</p></div></li>' for session in tutorial["schedule"]
        )
        link = self._icon_link(tutorial["url"], tutorial["link_label"], "globe")
        return (
            '<section class="highlight-tutorial" id="tutorial"><div>'
            f'<p class="eyebrow">{escape(tutorial["label"])}</p>'
            f'<h2>{escape(tutorial["title"])}</h2><p>{escape(tutorial["summary"])}</p>'
            f'<dl class="highlight-facts">{facts}</dl><div class="links">{link}</div></div>'
            f'<div class="highlight-topics"><p class="eyebrow">{escape(tutorial["topics_label"])}</p>'
            f'<ul>{topics}</ul></div>'
            '<div class="highlight-schedule">'
            f'<p class="eyebrow">{escape(tutorial["schedule_label"])}</p>'
            f'<h3>{escape(tutorial["schedule_title"])}</h3><p>{escape(tutorial["schedule_intro"])}</p>'
            f'<ol>{schedule}</ol></div></section>'
        )

    def _add_news_page(self, item: NewsItem) -> None:
        description = _plain_text(item["text"])
        self._add_search_record("News", f"{item['label']} · {item['date']}", f"news/{item['id']}.html", description)
        resources = self._news_resources(item)
        body = (
            _heading(item["label"], item["date"])
            + f'<div class="story"><div class="news-content"><p>{item["text"]}</p>{resources}</div>'
            '<a href="@/news/index.html">All news</a></div>'
        )
        self._add_page(f"news/{item['id']}.html", "News", item["label"], body, description)

    def _home_page(self, news: list[NewsItem]) -> str:
        sponsors = "".join(
            f'<a href="{escape(sponsor["url"])}"><img loading="lazy" src="@/{escape(sponsor["photo"])}" '
            f'alt="{escape(sponsor["name"])}"></a>'
            for sponsor in self._content.sponsors
        )
        selected = [paper for paper in self._content.papers if paper.get("selected")][:3]
        return self._home_template.substitute(
            news=self._news_rows(news[:5]),
            highlights="".join(self._highlight_entry(highlight) for highlight in self._content.highlights),
            papers="".join(self._paper_card(paper, self._content.authors) for paper in selected),
            sponsors=sponsors,
            github=self._icon_link("https://github.com/westlake-encode-lab", "GitHub", "github"),
            email=self._icon_link("mailto:encodelab@westlake.edu.cn", "Email", "envelope"),
            admission=self._icon_link("@/assets/pdf/admission.pdf", "Admission guide (PDF)", "file-pdf"),
            contact=self._icon_link("mailto:encodelab@westlake.edu.cn", "encodelab@westlake.edu.cn", "envelope"),
        )

    def _highlight_entry(self, highlight: Highlight) -> str:
        event = f"{highlight['venue']} {highlight['year']}"
        category = VENUE_CATEGORIES.get(highlight["venue"], "other")
        count = len(highlight["papers"])
        summary = f"{count} paper{'s' if count != 1 else ''}"
        if "tutorial" in highlight:
            summary += " · 1 tutorial"
        return (
            f'<a class="conference-entry" data-category="{category}" '
            f'href="@/highlights/{highlight["id"]}/index.html">'
            f'<h3>{escape(event)}</h3><p>{summary}</p>'
            '<span class="conference-entry-link">Explore highlights <span aria-hidden="true">→</span></span></a>'
        )

    def _icon_link(
        self,
        url: str,
        label: str,
        icon: str,
        *,
        icon_only: bool = False,
        person: str = "",
    ) -> str:
        name = f"{person} · {label}" if person else label
        css_class = "social-link" if icon_only else "icon-link"
        text = "" if icon_only else f"<span>{escape(label)}</span>"
        return (
            f'<a href="{escape(url)}" class="{css_class}" aria-label="{escape(name)}" '
            f'title="{escape(name)}">{self._icons[icon]}{text}</a>'
        )

    def _add_search_record(self, kind: str, title: str, url: str, keywords: str = "") -> None:
        self._search_records.append({"kind": kind, "title": title, "url": url, "keywords": keywords})

    def _people_page(self) -> str:
        groups = self._content.people
        sections = "".join(_link(f"#{_slug(group['group'])}", group["group"]) for group in groups)
        blocks = [
            _heading("People", "The people behind ENCODE Lab."),
            f'<nav class="section-nav" aria-label="People sections">{sections}</nav>',
        ]
        for group in groups:
            cards = []
            for person in group["people"]:
                name = person["name"]
                anchor = _slug(name)
                self._add_search_record("People", name, f"people/index.html#{anchor}", group["group"])
                if "photo" in person:
                    social_links = sorted(
                        person.get("links", {}).items(), key=lambda item: SOCIAL_ORDER.get(item[0], len(SOCIAL_ORDER))
                    )
                    links = " ".join(
                        self._icon_link(url, label, SOCIAL_ICONS.get(label, "globe"), icon_only=True, person=name)
                        for label, url in social_links
                    )
                    biography = "<br>".join(map(escape, person.get("bio", [])))
                    cards.append(
                        f'<article id="{anchor}" class="person">'
                        '<div class="portrait">'
                        f'<img loading="lazy" src="@/{escape(person["photo"])}" alt="" width="128" height="160"></div>'
                        f'<div class="person-content"><h3>{escape(name)}</h3><p>{biography}</p>'
                        f'<div class="social-links">{links}</div></div></article>'
                    )
                else:
                    display = _link(person["url"], name) if "url" in person else escape(name)
                    note = escape(person.get("note", ""))
                    cards.append(
                        f'<div class="member" id="{anchor}"><strong>{display}</strong><small>{note}</small></div>'
                    )
            layout = "profiles" if group["people"] and "photo" in group["people"][0] else "members"
            group_id = _slug(group["group"])
            heading = escape(group["group"])
            cards_html = "".join(cards)
            blocks.append(
                f'<section class="section-block" id="{group_id}"><h2>{heading}</h2>'
                f'<div class="{layout}">{cards_html}</div></section>'
            )
        return "".join(blocks)

    def _talks_page(self) -> str:
        blocks = [_heading("Talks", "Invited talks and seminars at Westlake ENCODE Lab.")]
        for talk in sorted(self._content.talks, key=lambda item: item["date"], reverse=True):
            anchor = _slug(talk["title"])
            day = date.fromisoformat(talk["date"])
            display_date = f"{day:%B} {day.day}, {day.year}"
            keywords = f"{talk['speaker']} {talk['affiliation']} {display_date}"
            self._add_search_record("Talks", talk["title"], f"talks/index.html#{anchor}", keywords)
            details = "".join(f"<li>{escape(detail)}</li>" for detail in talk["details"])
            speaker = _link(talk["homepage"], talk["speaker"])
            blocks.append(
                f'<article class="talk" id="{anchor}">'
                f'<p class="talk-date"><time datetime="{day}">{display_date}</time>'
                f'<span>{escape(talk["time"])}</span></p><h2>{escape(talk["title"])}</h2>'
                f'<div class="talk-speaker"><strong>{speaker}</strong><span>{escape(talk["role"])}</span>'
                f'<p>{escape(talk["affiliation"])}</p></div>'
                f'<ul class="talk-details">{details}</ul>'
                f'<div class="portrait"><img loading="lazy" src="@/{escape(talk["photo"])}" '
                'alt="" width="128" height="160"></div>'
                f'<p class="talk-abstract">{escape(talk["abstract"])}</p></article>'
            )
        return "".join(blocks)

    def _news_rows(self, items: list[NewsItem]) -> str:
        rows = []
        for item in items:
            display_date = date.fromisoformat(item["date"]).strftime("%b %d, %Y")
            resources = self._news_resources(item)
            rows.append(
                f'<article class="news-row" id="{item["id"]}">'
                f'<time datetime="{item["date"]}">{display_date}</time>'
                f'<div><a class="news-label" href="@/news/{item["id"]}.html">{escape(item["label"])}</a>'
                f"<p>{item['text']}</p>{resources}</div></article>"
            )
        return "".join(rows)

    def _news_resources(self, item: NewsItem) -> str:
        resources = []
        if "arxiv" in item:
            resources.append(self._icon_link(f"https://arxiv.org/abs/{item['arxiv']}", "arXiv", "arxiv"))
        if "code" in item:
            icon = "github" if urlsplit(item["code"]).hostname == "github.com" else "code"
            resources.append(self._icon_link(item["code"], "Code", icon))
        if not resources:
            return ""
        links = "".join(resources)
        return f'<div class="links news-resources">{links}</div>'

    def _news_page(self, items: list[NewsItem]) -> str:
        years = sorted({item["date"][:4] for item in items}, reverse=True)
        links = " ".join(_link(f"#year-{year}", year) for year in years)
        blocks = [
            _heading("News", "Research, milestones and updates from the lab."),
            f'<nav class="section-nav" aria-label="News years">{links}</nav>',
        ]
        for year in years:
            rows = self._news_rows([item for item in items if item["date"].startswith(year)])
            blocks.append(f'<section class="news-year"><h2 id="year-{year}">{year}</h2><div>{rows}</div></section>')
        return "".join(blocks)

    def _paper_card(self, paper: Paper, authors: dict[str, str]) -> str:
        names = [_author_name(author) for author in paper["author"].split(" and ")]
        author_links = []
        for name in names:
            label = _link(authors[name], name) if name in authors else escape(name)
            author_links.append(f"<strong>{label}</strong>" if name == "Huan Wang" else label)
        byline = ", ".join(author_links)
        venue = escape(paper.get("booktitle") or paper.get("journal", ""))
        resources = []
        if "pdf" in paper:
            resources.append(self._icon_link(paper["pdf"], "PDF", "file-pdf"))
        if "arxiv" in paper:
            resources.append(self._icon_link(f"https://arxiv.org/abs/{paper['arxiv']}", "arXiv", "arxiv"))
        if "website" in paper:
            resources.append(self._icon_link(paper["website"], "Project", "globe"))
        if "code" in paper:
            icon = "github" if urlsplit(paper["code"]).hostname == "github.com" else "code"
            resources.append(self._icon_link(paper["code"], "Code", icon))
        links = " ".join(resources)
        selected = int(paper.get("selected", False))
        title_url = paper.get("pdf") or paper.get("website")
        if not title_url and "arxiv" in paper:
            title_url = f"https://arxiv.org/abs/{paper['arxiv']}"
        title = _link(title_url, paper["title"]) if title_url else escape(paper["title"])
        citation = escape(_bibliography(paper))
        category = VENUE_CATEGORIES.get(paper["abbr"], "journal" if paper["type"] == "article" else "other")
        return (
            f'<article class="paper" id="{paper["id"]}" data-year="{paper["year"]}" data-selected="{selected}">'
            f'<span class="venue" data-category="{category}">{escape(paper["abbr"])}</span>'
            f'<div class="paper-content"><h3>{title}</h3>'
            f'<p class="authors">{byline}</p><p class="venue-name">{venue}, {paper["year"]}</p>'
            f'<div class="links">{links}<details><summary>{self._icons["code"]}<span>BibTeX</span></summary>'
            f"<pre>{citation}</pre></details></div></div></article>"
        )

    def _publications_page(self, papers: list[Paper], authors: dict[str, str]) -> str:
        years = sorted({paper["year"] for paper in papers}, reverse=True)
        options = "".join(f'<option value="{year}">{year}</option>' for year in years)
        blocks = [
            _heading("Publications", "Research from ENCODE Lab, with papers, code and project resources."),
            (
                '<ul class="venue-key" aria-label="Publication categories">'
                '<li data-category="vision">Computer vision</li><li data-category="learning">Machine learning</li>'
                '<li data-category="journal">Journals</li><li data-category="preprint">arXiv preprints</li>'
                '<li data-category="other">Other conferences</li></ul>'
            ),
            (
                '<div class="pub-controls" hidden>'
                '<label>Search publications<input type="search" id="filter" placeholder="Title, author or venue"></label>'
                f'<label>Year<select id="pub-year"><option value="all">All years</option>{options}</select></label>'
                '<label>Collection<select id="collection"><option value="all">All publications</option>'
                '<option value="selected">Selected publications</option></select></label>'
                '<div class="filter-status"><output id="pub-count" aria-live="polite"></output>'
                '<button id="reset-filters" type="button">Reset filters</button></div></div>'
            ),
        ]
        for year in years:
            entries = []
            for paper in (paper for paper in papers if paper["year"] == year):
                keywords = f"{paper['author']} {paper['abbr']} {year}"
                self._add_search_record(
                    "Publications",
                    paper["title"],
                    f"publications/index.html#{paper['id']}",
                    keywords,
                )
                entries.append(self._paper_card(paper, authors))
            cards = "".join(entries)
            blocks.append(f'<section class="year-group"><h2 id="year-{year}">{year}</h2><div>{cards}</div></section>')
        bibliography_link = _link("@/assets/papers.bib", "Download full bibliography (.bib)")
        blocks.append(f'<p id="no-papers" hidden>No publications match your search.</p><p>{bibliography_link}</p>')
        return "".join(blocks)

    def _gallery_page(self) -> str:
        photos = sorted(
            path for path in (self._root / "assets/img/gallery").iterdir()
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".avif"}
        )
        thumbnails = []
        for number, path in enumerate(photos, start=1):
            source = f"@/{escape(path.relative_to(self._root).as_posix())}"
            thumbnails.append(
                f'<a href="{source}" data-photo>'
                f'<img src="{source}" alt="Gallery photo {number}" loading="lazy" decoding="async"></a>'
            )
        images = "".join(thumbnails)
        return (
            _heading("Gallery")
            + f'<div class="gallery">{images}</div>'
            '<dialog id="lightbox" aria-label="Photo viewer">'
            '<div class="photo-actions"><a id="photo-original" target="_blank" rel="noopener">Open original</a>'
            '<button type="button" data-close>Close</button></div><div class="photo-stage"><img alt=""></div>'
            '<div class="photo-controls">'
            '<button type="button" id="previous" aria-label="Previous photo">Previous</button>'
            '<output id="photo-count" aria-live="polite" aria-atomic="true"></output>'
            '<button type="button" id="next" aria-label="Next photo">Next</button></div></dialog>'
        )

def _plain_text(html: str) -> str:
    return unescape(re.sub("<[^>]+>", "", html))

def _link(url: str, label: str) -> str:
    return f'<a href="{escape(url)}">{escape(label)}</a>'

def _heading(name: str, subtitle: str = "") -> str:
    caption = f"<p>{escape(subtitle)}</p>" if subtitle else ""
    return f'<header class="page-heading"><h1>{escape(name)}</h1>{caption}</header>'

def _slug(text: str) -> str:
    return re.sub("[^a-z0-9]+", "-", text.lower()).strip("-")

def _author_name(raw: str) -> str:
    return " ".join(reversed(raw.split(", ", 1)))

def _bibliography(paper: Paper) -> str:
    fields = {
        "title": paper["title"],
        "author": paper["author"],
        "booktitle": paper.get("booktitle"),
        "journal": paper.get("journal"),
        "year": paper["year"],
    }
    lines = [f"  {field} = {{{value}}}" for field, value in fields.items() if value is not None]
    entries = ",\n".join(lines)
    return f"@{paper['type']}{{{paper['id']},\n{entries}\n}}"
