"""Reveal.js operator."""

from playwright.sync_api import Page, ViewportSize


class SlideOperator:
    def __init__(self, page: Page):
        self._page = page
        self._size: ViewportSize

    def setup_slide(self):
        """Procedure before capture."""
        # NOTE: It may be should do as optional.
        self._page.evaluate("Reveal.configure({progress: false});")
        if self._page.viewport_size:
            self._size = self._page.viewport_size

    def capture(self) -> bytes:
        return self._page.pdf(
            width=str(self._size["width"]),
            height=str(self._size["height"]),
            print_background=True,
        )

    def forward_slide(self):
        """Forward next slide."""
        self._page.evaluate("Reveal.next();")
