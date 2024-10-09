"""Entrypoint of CLI."""

import io
import subprocess
from pathlib import Path
from typing import List

import click
from playwright.sync_api import Page, sync_playwright
from pypdf import PdfReader, PdfWriter

from .slides import revealjs


def collect_slides(page: Page, url: str) -> List[bytes]:
    slides = []
    page.emulate_media(media="screen")
    page.goto(url)
    # NOTE: Works only Reveal.js presentation
    operator = revealjs.SlideOperator(page)
    operator.setup_slide()
    size = page.viewport_size
    if size is None:
        raise Exception("Viewport is None")
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
def main(url: str, dest: Path):
    """Generate PDF file from URL to DEST."""
    with sync_playwright() as p:
        if not Path(p.chromium.executable_path).exists():
            print(
                "Chromium is not exists on Playwright. Now downloading automatically..."
            )
            subprocess.run("playwright install chromium".split())

        browser = p.chromium.launch()
        page = browser.new_page()
        slides = collect_slides(page, url)
        browser.close()

    writer = PdfWriter()
    for slide in slides:
        reader = PdfReader(io.BytesIO(slide))
        writer.add_page(reader.pages[0])
    writer.write(dest)
    writer.close()
