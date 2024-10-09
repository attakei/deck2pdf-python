"""Reveal.js operator."""

from playwright.sync_api import Page

from ._base import SlideReaderBase


def resolve_format(page: Page) -> bool:
    return page.evaluate("typeof Reveal") != "undefined"


class SlideReader(SlideReaderBase):
    def setup_slide(self, script: str):
        """Procedure before capture."""
        # NOTE: It may be should do as optional.
        self._page.evaluate("Reveal.configure({progress: false});")
        self._page.evaluate(script)
        # Reveal.js can set viewport from config.
        # It catches this as "best presentation size".
        if self._page.viewport_size:
            self._size = self._page.viewport_size

    def forward_slide(self):
        """Forward next slide."""
        self._page.evaluate("Reveal.next();")
