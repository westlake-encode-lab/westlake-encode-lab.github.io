"""Build the lab website and publish a complete local output directory."""

import argparse
import json
import shutil
from datetime import date
from html import escape
from pathlib import Path
from tempfile import TemporaryDirectory

from site_content import load_content
from site_render import SITE_ORIGIN, RenderedSite, SiteRenderer

PROJECT_ROOT = Path(__file__).resolve().parent

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", action="store_true", help="Include a local overview of all six pages")
    arguments = parser.parse_args()
    output = build_site(PROJECT_ROOT, preview=arguments.preview)
    print(f"Built website in {output}")
    if arguments.preview:
        print(f"Preview overview: {output / 'preview.html'}")

def build_site(root: Path, *, preview: bool = False) -> Path:
    content = load_content(root / "content")
    rendered = SiteRenderer(root, content, date.today()).render_site()
    output = root / "_site"

    with TemporaryDirectory(prefix=".site-build-", dir=root) as temporary:
        staging = Path(temporary) / "site"
        shutil.copytree(root / "assets", staging / "assets")
        _write_site(staging, rendered)
        if preview:
            shutil.copyfile(root / "templates/preview.html", staging / "preview.html")
        _replace_output(staging, output, Path(temporary) / "previous")
    return output

def _write_site(directory: Path, rendered: RenderedSite) -> None:
    files = dict(rendered.pages)
    files[".nojekyll"] = ""
    files["assets/papers.bib"] = rendered.bibliography
    search_json = json.dumps(rendered.search_records, ensure_ascii=False)
    files["assets/search-index.js"] = f"window.labSearch = {search_json};\n"
    files["robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {SITE_ORIGIN}/sitemap.xml\n"
    locations = [f"{SITE_ORIGIN}/{path.removesuffix('index.html')}" for path in rendered.pages if path != "404.html"]
    sitemap_entries = "".join(f"<url><loc>{escape(location)}</loc></url>\n" for location in locations)
    files["sitemap.xml"] = f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_entries}</urlset>\n'

    for path, text in files.items():
        destination = directory / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")

def _replace_output(staging: Path, output: Path, previous: Path) -> None:
    if output.exists():
        output.rename(previous)
    try:
        staging.rename(output)
    except OSError:
        # Restore the last successful build if publishing the staged directory fails.
        if previous.exists():
            previous.rename(output)
        raise

if __name__ == "__main__":
    main()
