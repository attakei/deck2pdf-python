"""Abstract module for operator."""

from typing import List, Optional
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

    def capture_all(self) -> List[bytes]:
        """Fetch all pages as byte-stream."""
        slides = []
        while True:
            content = self.capture()
            if slides and slides[-1] == content:
                break
            slides.append(content)
            self.forward_slide()
        return slides

    def setup_slide(self, script: str):
        """Procedure before starting capture."""

    def forward_slide(self):
        """Forward next slide."""
        self._page.keyboard.type(" ")
