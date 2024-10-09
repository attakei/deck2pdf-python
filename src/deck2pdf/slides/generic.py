"""General slide operator."""

from ._base import SlideReaderBase


class SlideReader(SlideReaderBase):
    def setup_slide(self):
        self._page.evaluate(self._setup)
