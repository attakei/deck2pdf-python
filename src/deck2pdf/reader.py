"""Reading core functions."""

import importlib
import sys
from pathlib import Path
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
    page.emulate_media(media="screen")
    page.goto(url)
    if format is None:
        for c in CANDICATES:
            cm = importlib.import_module(f"..slides.{c}", __name__)
            if cm.resolve_format(page):
                format = c
                break
    if format == "custom":
        module_path = "custom"
        sys.path.append(str(Path.cwd()))
    else:
        module_path = f"..slides.{format}"
    module = importlib.import_module(module_path, __name__)
    return module.SlideReader(page, size)
