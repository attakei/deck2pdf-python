"""Writing functions."""

import io
from pathlib import Path
from typing import List

from pypdf import PdfReader, PdfWriter


def write_pdf(out: Path, slides: List[bytes]):
    """Generate PDF file from slides' bytestream."""
    print(f"Save as {out}")
    writer = PdfWriter()
    for slide in slides:
        reader = PdfReader(io.BytesIO(slide))
        writer.add_page(reader.pages[0])
    writer.write(out)
    writer.close()
