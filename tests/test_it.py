from pathlib import Path

from click.testing import CliRunner
from deck2pdf.cli import main


def test_as_simple_e2e(tmp_path: Path):
    url = "https://slides.attakei.net/pyconjp-2022/"
    dest = tmp_path / "output.pdf"
    runner = CliRunner()
    result = runner.invoke(main, [url, str(dest)])
    assert result.exit_code == 0
    assert dest.exists()
