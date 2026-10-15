# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import tomllib
from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "poe-tasks-common"
author = "Jonathan King"
copyright = f"%Y, {author}"

# Parse the release string from pyproject.toml
_pyproject = Path(__file__).parents[1] / "pyproject.toml"
with open(_pyproject, "rb") as file:
    _pyproject = tomllib.load(file)
release = _pyproject["project"]["version"]
version = ".".join(release.split(".")[:-1])


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design", "sphinx_copybutton"]
highlight_language = "none"
pygments_style = "sphinx"

# Common links
rst_prolog = "\n".join(
    [
        ".. _poethepoet: https://poethepoet.natn.io/",
        ".. _poe: https://poethepoet.natn.io/",
        ".. _uv: https://docs.astral.sh/uv/",
        ".. _pre-commit: https://pre-commit.com/",
        ".. _pip-audit: https://pypi.org/project/pip-audit/",
        ".. _ruff: https://docs.astral.sh/ruff/",
        ".. _pytest: https://docs.pytest.org/en/stable/",
        ".. _coverage: https://coverage.readthedocs.io/en/latest/",
        ".. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/",
        ".. _sphinx: https://www.sphinx-doc.org/en/master/index.html",
        ".. _black: https://black.readthedocs.io/en/stable/",
        ".. _isort: https://isort.readthedocs.io/en/latest/",
    ]
)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_copy_source = False
html_theme = "furo"
html_title = f"{project} {release}"
