import os

from deck2pdf import __version__ as version

# -- Project information
project = "deck2pdf"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    "sphinx.ext.todo",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for i18n
locale_dirs = ["_locales"]
gettext_compact = False
gettext_language_team = "Kazuya Takei <myself@attakei.net>"
gettext_last_translator = os.environ.get("SPHINXINTL_TRANSLATOR", None)

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
