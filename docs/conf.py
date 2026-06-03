"""Sphinx configuration."""

project = "openQEvo"
copyright = "2026, QSC Software Thrust"
author = "QSC Software Thrust"

extensions = ["myst_parser"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "sphinx_rtd_theme"

suppress_warnings = ["misc.highlighting_failure"]
