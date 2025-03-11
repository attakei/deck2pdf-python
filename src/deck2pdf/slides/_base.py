"""Abstract module for operator."""

import time
from typing import List, Optional
from playwright.sync_api import Page, ViewportSize


class SlideReaderBase:
    """Base class for handle slider html."""

    def __init__(
        self,
        page: Page,
        size: Optional[ViewportSize] = None,
    ):
        self._slides: list[bytes] = []
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
        print("Capture ... ", end="")
        while True:
            content = self.capture()
            self._slides.append(content)
            print(f"\rCapture ... {len(self._slides)} slides.", end="")
            if self.is_last_slide(content):
                self.post_last_slide()
                break
            # TODO: Optional?
            time.sleep(1)
            self.forward_slide()
        return self._slides

    def setup_slide(self, script: str):
        """Procedure before starting capture."""

    def is_last_slide(self, content: bytes) -> bool:
        return self._slides[-2] == content

    def post_last_slide(self):
        self._slides.pop()

    def forward_slide(self):
        """Forward next slide."""
        self._page.keyboard.type(" ")
