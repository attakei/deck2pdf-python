"""Reading core functions."""

import importlib
from typing import Optional
from playwright.sync_api import Page

from ._types import Size
from .slides._base import SlideReaderBase


CANDICATES = [
    "revealjs",
    "generic",
]


def init_reader(
    page: Page,
    url: str,
    format: Optional[str] = None,
    size: Optional[Size] = None,
) -> SlideReaderBase:
    print(f"Fetch {url} ...", end="")
    page.emulate_media(media="screen")
    page.goto(url)
    page.wait_for_load_state("load")
    print(f"\rFetch {url} ... loaded.")
    if format is None:
        for c in CANDICATES:
            cm = importlib.import_module(f"..slides.{c}", __name__)
            if cm.resolve_format(page):
                format = c
                break
    module = importlib.import_module(f"..slides.{format}", __name__)
    print(f"Use '{module.__name__}' format")
    return module.SlideReader(page, size)
