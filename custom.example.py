"""Example of custom operator.

If you want to try it, put this file into CWD as ``custom.py`` and
run deck2pdf with ``--format=custom`` option.
"""

from deck2pdf.slides._base import SlideReaderBase


class SlideReader(SlideReaderBase):
    """Example reader.

    Rule:

    * Wait 2 secs each before capture page.
    * Capture 8 pages.
    """

    SLIDES = 8

    def capture_all(self):
        """Fetch all pages as byte-stream."""
        slides = []
        for p in range(1, 1 + self.SLIDES):
            self._page.wait_for_timeout(2000)
            content = self.capture()
            slides.append(content)
            self.forward_slide()
        return slides
