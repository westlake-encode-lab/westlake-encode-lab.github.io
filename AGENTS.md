# Westlake ENCODE Lab website

The site uses Python 3.12 or newer and the standard library. Run `python3 build.py --preview` for local review. Generated output lives in `_site/`.

Apply the user's code conventions to project-owned Python. Annotate every function parameter and return value, dataclass field and instance attribute. Use native types, descriptive names, private helper prefixes, one-line English module docstrings and 120-character lines. Leave one blank line between top-level definitions and between methods. Keep `__main__` blocks limited to one entry-point call. Catch specific errors only at a boundary that can act on them.

Keep data loading, page rendering and filesystem publication in their owning modules. Preserve public URLs, publication IDs and lab-owned media. Keep third-party icons and fonts in their source formats with their licenses. Keep comments in Python code only.

Before delivery, read the modified source and run the build documented in README.md. For changes to layouts, links or interactions, verify the affected pages in the generated site. Report which checks ran.

Keep publication metadata to title, authors, venue and year. Resource links are optional. Use one social-link order across profiles.

Group papers by year, newest first. Within each year, list accepted papers by acceptance date (publication date if unknown), then preprints by first submission date. Verify acceptance or publication timing before inserting a paper; adding it today does not make it the newest result. Preserve the precision of the source, distinguish news posting dates from conference decisions, and never use an arXiv revision date as an acceptance date.

Conference highlights reference existing publication IDs for scope validation, but preserve the presentation content from each recorded source page. Keep its titles, author emphasis and equal-contribution markers, summaries, resource links and pending statuses, schedules, and participant lists. Do not overwrite these with the main bibliography or other websites. New highlight records automatically appear in the homepage's Conference highlights section; also link the corresponding announcement.

Derive venue colors from their category; arXiv resources do not turn accepted papers into preprints. Keep all person portraits the same size at a given viewport, including the principal investigator, using the shared 4:5 portrait frame on People, Talks and conference pages. Landscape photo thumbnails and research-figure frames use the shared landscape token. Research figures must remain fully visible inside their uniform frames. Conference cover images and banners use their intrinsic aspect ratios with automatic height; never force them into a golden-ratio container that adds blank space or crops embedded text.

The user excluded FreeBlend, Proteus, LightDP, MobileSCI and SSD. Do not re-add them. Corresponding authorship, last authorship and university affiliation alone do not establish that a paper belongs in the lab's publication collection.
