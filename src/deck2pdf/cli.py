"""Entrypoint of CLI."""

import io
import re
import subprocess
from pathlib import Path
from typing import List, Optional, TypedDict

import click
from playwright.sync_api import Page, sync_playwright
from pypdf import PdfReader, PdfWriter

from .slides import resolve_slide


class Size(TypedDict):
    width: int
    height: int


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
    format: str,
    size: Optional[Size] = None,
) -> List[bytes]:
    slides = []
    page.emulate_media(media="screen")
    page.goto(url)
    slide_module = resolve_slide(format)
    operator = slide_module.SlideReader(page, size)
    operator.setup_slide()
    while True:
        content = operator.capture()
        if slides and slides[-1] == content:
            break
        slides.append(content)
        operator.forward_slide()
    return slides


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
    required=False,
    default="generic",
    help="Presentation format (using tool)",
)
def main(
    url: str,
    dest: Path,
    format: str,
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
        slides = collect_slides(page, url, format, size)
        browser.close()

    writer = PdfWriter()
    for slide in slides:
        reader = PdfReader(io.BytesIO(slide))
        writer.add_page(reader.pages[0])
    writer.write(dest)
    writer.close()
