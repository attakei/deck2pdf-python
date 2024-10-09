"""Abstract module for operator."""

from typing import Optional
from playwright.sync_api import Page, ViewportSize


class SlideReaderBase:
    """Base class for handle slider html."""

    def __init__(
        self,
        page: Page,
        size: Optional[ViewportSize] = None,
    ):
        self._page = page
        if size:
            self._size: ViewportSize = size

    def capture(self) -> bytes:
        """Generate PDF data from current slide."""
        return self._page.pdf(
            width=str(self._size["width"]),
            height=str(self._size["height"]),
            print_background=True,
        )

    def setup_slide(self):
        """Procedure before starting capture."""
        pass

    def forward_slide(self):
        """Forward next slide."""
        self._page.keyboard.type(" ")
