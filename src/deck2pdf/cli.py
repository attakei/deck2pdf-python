"""Entrypoint of CLI."""

import re
import subprocess
from pathlib import Path
from typing import List, Optional

import click
from playwright.sync_api import Page, sync_playwright


from ._types import Size
from .reader import init_reader
from .writer import write_pdf


def parse_size(ctx, param, val: Optional[str] = None) -> Optional[Size]:
    if val is None:
        return None
    matched = re.match(r"(?P<width>\d+)x(?P<height>\d+)", val)
    if matched is None:
        raise click.BadParameter("Format must be WIDTHxHEIGHT.")
    return Size(width=int(matched.group("width")), height=int(matched.group("height")))


def collect_slides(
    page: Page,
    url: str,
    setup: str = "",
    format: Optional[str] = None,
    size: Optional[Size] = None,
) -> List[bytes]:
    reader = init_reader(page, url, format, size)
    reader.setup_slide(setup)
    return reader.capture_all()


@click.command()
@click.argument("url", type=str)
@click.argument(
    "dest",
    type=click.Path(
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "--size",
    type=click.UNPROCESSED,
    callback=parse_size,
    help="Pixel size of pdf ([WIDTH]x[HEIGHT] style)",
)
@click.option(
    "--format",
    type=str,
    help="Presentation format (using tool)",
)
@click.option(
    "--setup",
    type=str,
    default="",
    help="Scripts before starting capture.",
)
def main(
    url: str,
    dest: Path,
    setup: str,
    format: Optional[str] = None,
    size: Optional[Size] = None,
):
    """Generate PDF file from URL to DEST."""
    with sync_playwright() as p:
        if not Path(p.chromium.executable_path).exists():
            print(
                "Chromium is not exists on Playwright. Now downloading automatically..."
            )
            subprocess.run("playwright install chromium".split())

        browser = p.chromium.launch()
        page = browser.new_page()
        # TODO: Implement more clearly
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "file://" + str(Path(url).resolve())
        slides = collect_slides(page, url, setup, format, size)
        browser.close()

    write_pdf(dest, slides)
