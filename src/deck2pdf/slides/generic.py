"""General slide operator."""

from typing import Optional
from playwright.sync_api import Page, ViewportSize


class SlideOperator:
    def __init__(self, page: Page, size: Optional[ViewportSize] = None):
        self._page = page
        if size:
            self._size: ViewportSize = size

    def setup_slide(self):
        """Procedure before capture."""
        pass

    def capture(self) -> bytes:
        return self._page.pdf(
            width=str(self._size["width"]),
            height=str(self._size["height"]),
            print_background=True,
        )

    def forward_slide(self):
        """Forward next slide."""
        self._page.keyboard.type(" ")
