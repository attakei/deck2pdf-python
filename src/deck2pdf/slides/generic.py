"""General slide operator."""

from playwright.sync_api import Page
from ._base import SlideReaderBase


def resolve_format(page: Page) -> bool:
    return True


class SlideReader(SlideReaderBase):
    def setup_slide(self, script: str):
        self._page.evaluate(script)
