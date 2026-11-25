"""Define and load the lab's structured website content."""

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import NotRequired, TypedDict, cast


class Person(TypedDict):
    name: str
    photo: NotRequired[str]
    bio: NotRequired[list[str]]
    links: NotRequired[dict[str, str]]
    url: NotRequired[str]
    note: NotRequired[str]

class PeopleGroup(TypedDict):
    group: str
    people: list[Person]

class Paper(TypedDict):
    id: str
    type: str
    abbr: str
    title: str
    author: str
    year: str
    pdf: NotRequired[str]
    booktitle: NotRequired[str]
    journal: NotRequired[str]
    arxiv: NotRequired[str]
    website: NotRequired[str]
    code: NotRequired[str]
    selected: NotRequired[bool]

class NewsItem(TypedDict):
    id: str
    date: str
    label: str
    text: str
    arxiv: NotRequired[str]
    code: NotRequired[str]

class Talk(TypedDict):
    title: str
    speaker: str
    role: str
    affiliation: str
    date: str
    time: str
    abstract: str
    photo: str
    details: list[str]
    homepage: str

class Sponsor(TypedDict):
    url: str
    name: str
    photo: str

class HighlightResource(TypedDict):
    label: str
    url: NotRequired[str]

class HighlightPaper(TypedDict):
    paper_id: str
    title: str
    authors_html: str
    topic: str
    resources: list[HighlightResource]
    summary_html: NotRequired[str]
    session: NotRequired[str]
    image: NotRequired[str]
    image_alt: NotRequired[str]
    image_caption: NotRequired[str]

class HighlightPerson(TypedDict):
    name: str
    photo: str
    contribution: str
    url: str
    role: NotRequired[str]

class HighlightTopic(TypedDict):
    title: str
    summary: str

class HighlightSession(TypedDict):
    time: str
    title: str
    speaker: str

class HighlightTutorial(TypedDict):
    label: str
    title: str
    url: str
    link_label: str
    summary: str
    facts: dict[str, str]
    topics_label: str
    topics: list[HighlightTopic]
    schedule_label: str
    schedule_title: str
    schedule_intro: str
    schedule: list[HighlightSession]

class Highlight(TypedDict):
    id: str
    venue: str
    year: str
    source_url: str
    eyebrow: str
    headline_html: str
    introduction_html: str
    tags: list[str]
    keywords: list[str]
    image: str
    image_width: int
    image_height: int
    image_alt: str
    image_credit: str
    papers_heading: str
    papers: list[HighlightPaper]
    people_kicker: str
    people_title: str
    people_intro: str
    people: list[HighlightPerson]
    host: NotRequired[HighlightPerson]
    tutorial: NotRequired[HighlightTutorial]

class SearchRecord(TypedDict):
    kind: str
    title: str
    url: str
    keywords: str

@dataclass(frozen=True)
class SiteContent:
    people: list[PeopleGroup]
    papers: list[Paper]
    news: list[NewsItem]
    talks: list[Talk]
    sponsors: list[Sponsor]
    authors: dict[str, str]
    highlights: list[Highlight]

def load_content(directory: Path) -> SiteContent:
    content = SiteContent(
        people=cast(list[PeopleGroup], _load_records(directory / "people.json")),
        papers=cast(list[Paper], _load_records(directory / "papers.json")),
        news=cast(list[NewsItem], _load_records(directory / "news.json")),
        talks=cast(list[Talk], _load_records(directory / "talks.json")),
        sponsors=cast(list[Sponsor], _load_records(directory / "sponsors.json")),
        authors=_load_authors(directory / "authors.json"),
        highlights=cast(list[Highlight], _load_records(directory / "highlights.json")),
    )
    _validate_content(content)
    return content

def _load_records(path: Path) -> list[dict[str, object]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or not all(isinstance(record, dict) for record in value):
        raise ValueError(f"{path}: expected a list of records")
    return value

def _load_authors(path: Path) -> dict[str, str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not all(
        isinstance(name, str) and isinstance(url, str) for name, url in value.items()
    ):
        raise ValueError(f"{path}: expected a mapping of author names to URLs")
    return value

def _validate_content(content: SiteContent) -> None:
    for paper in content.papers:
        if not paper.get("booktitle") and not paper.get("journal"):
            raise ValueError(f"Paper {paper['id']}: a booktitle or journal is required")
        if "selected" in paper and not isinstance(paper["selected"], bool):
            raise ValueError(f"Paper {paper['id']}: selected must be a boolean")

    for item in content.news:
        date.fromisoformat(item["date"])

    papers_by_id = {paper["id"]: paper for paper in content.papers}
    for highlight in content.highlights:
        identifiers = [item["paper_id"] for item in highlight["papers"]]
        if not identifiers or len(identifiers) != len(set(identifiers)):
            raise ValueError(f"Highlight {highlight['id']}: papers must be nonempty and unique")
        for identifier in identifiers:
            if identifier not in papers_by_id:
                raise ValueError(f"Highlight {highlight['id']}: unknown paper {identifier}")
            paper = papers_by_id[identifier]
            if (paper["abbr"], paper["year"]) != (highlight["venue"], highlight["year"]):
                raise ValueError(f"Highlight {highlight['id']}: paper {identifier} has a different venue or year")
        for feature in highlight["papers"]:
            if "image" in feature and not feature.get("image_alt"):
                raise ValueError(f"Highlight {highlight['id']}: research figures require alternative text")

    for group in content.people:
        profiles = ["photo" in person for person in group["people"]]
        if profiles and any(profiles) != all(profiles):
            raise ValueError(f"People group {group['group']}: use a consistent profile layout")
        for person in group["people"]:
            if "photo" in person and ("bio" not in person or "links" not in person):
                raise ValueError(f"Person {person['name']}: photo profiles require bio and links")

    for name, records in (("papers", content.papers), ("news", content.news), ("highlights", content.highlights)):
        identifiers = [record["id"] for record in records]
        if len(identifiers) != len(set(identifiers)):
            raise ValueError(f"{name}: IDs must be unique")
        for identifier in identifiers:
            if not identifier or "/" in identifier or "\\" in identifier or identifier in {".", ".."}:
                raise ValueError(f"{name}: invalid ID {identifier!r}")
