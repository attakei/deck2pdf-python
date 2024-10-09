"""Reveal.js operator."""

from ._base import SlideReaderBase


class SlideReader(SlideReaderBase):
    def setup_slide(self):
        """Procedure before capture."""
        # NOTE: It may be should do as optional.
        self._page.evaluate("Reveal.configure({progress: false});")
        # Reveal.js can set viewport from config.
        # It catches this as "best presentation size".
        if self._page.viewport_size:
            self._size = self._page.viewport_size

    def forward_slide(self):
        """Forward next slide."""
        self._page.evaluate("Reveal.next();")
