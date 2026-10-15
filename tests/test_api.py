import pytest

from poe_tasks_common import tasks


@pytest.fixture
def schema():
    return {
        "groups": {
            "100_setup": {
                "heading": "Setup:",
                "tasks": {
                    "setup": {
                        "help": "Syncs all dependencies and installs pre-commit",
                        "default_item_type": "ref",
                        "sequence": ["sync --frozen", "install-precommit"],
                    },
                    "install-precommit": {
                        "help": "Installs pre-commit",
                        "default_item_type": "cmd",
                        "sequence": [
                            "uv tool install pre-commit --with pre-commit-uv --force-reinstall",
                            "pre-commit install",
                        ],
                    },
                },
            },
            "200_env": {
                "heading": "Environment:",
                "tasks": {
                    "sync": {
                        "help": "Syncs the development environment",
                        "cmd": "uv sync --all-groups --all-extras",
                    },
                    "upgrade": {
                        "help": "Syncs and upgrades the development environment",
                        "ref": "sync --upgrade",
                    },
                },
            },
            "300_security": {
                "heading": "Security:",
                "tasks": {
                    "audit": {
                        "help": "Check package dependencies for security issues",
                        "cmd": "pip-audit",
                    }
                },
            },
            "400_lint": {
                "heading": "Linting:",
                "tasks": {
                    "format": {
                        "help": "Formats the code and its tests",
                        "default_item_type": "cmd",
                        "sequence": [
                            "ruff format src tests",
                            "ruff check src tests --select I --fix",
                        ],
                    },
                    "lint": {
                        "help": "Lints the code and its tests",
                        "cmd": "ruff check src tests",
                    },
                },
            },
            "500_test": {
                "heading": "Testing:",
                "tasks": {
                    "tests": {
                        "help": "Runs the tests and requires a minimum coverage",
                        "sequence": [
                            {
                                "cmd": "pytest tests --cov=src --cov=tests --cov-fail-under=${_min_coverage} --cov-report xml:coverage.xml"
                            },
                            {"ref": "coverage"},
                        ],
                        "args": [
                            {
                                "name": "_min_coverage",
                                "help": "Minimum required test coverage percent",
                                "options": ["--min-coverage"],
                                "type": "string",
                                "default": "${MIN_COVERAGE:-100}",
                            }
                        ],
                    },
                    "htmlcov": {
                        "help": "Builds an HTML coverage report and opens in a web browser",
                        "sequence": [
                            {"ref": "_rmtree htmlcov"},
                            {"cmd": "coverage html --skip-covered"},
                            {"ref": "_browse-index htmlcov"},
                        ],
                    },
                    "coverage": {
                        "help": "Prints the coverage report for the tests",
                        "cmd": "coverage report",
                    },
                },
            },
            "600_docs": {
                "heading": "Documentation:",
                "tasks": {
                    "docs": {
                        "help": "Rebuilds the documentation",
                        "sequence": [
                            {"ref": "_rmtree ${_output_folder}"},
                            {"cmd": "sphinx-build -qa docs ${_output_folder}"},
                        ],
                        "args": [
                            {
                                "help": "Folder containing the built documentation",
                                "name": "_output_folder",
                                "options": ["-o", "--output"],
                                "default": "${DOCS_OUTPUT:-public}",
                            }
                        ],
                    },
                    "open-docs": {
                        "help": "Opens the built documentation in a web browser",
                        "ref": "_browse-index ${_output_folder}",
                        "args": [
                            {
                                "help": "Folder containing the built documentation",
                                "name": "_output_folder",
                                "options": ["-o", "--output"],
                                "default": "${DOCS_OUTPUT:-public}",
                            }
                        ],
                    },
                },
            },
        },
        "tasks": {
            "_browse": {
                "help": "Opens a URI (file or web URL) in a web browser",
                "expr": "webbrowser.open(_uri)",
                "imports": ["webbrowser"],
                "args": [
                    {
                        "name": "_uri",
                        "help": "The target URI (file or web URL) to open",
                        "positional": True,
                        "required": True,
                    }
                ],
            },
            "_browse-file": {
                "help": "Opens a project file in a web browser",
                "expr": "webbrowser.open( pathlib.Path(_path).resolve().as_uri() )",
                "imports": ["webbrowser", "pathlib"],
                "args": [
                    {
                        "name": "_path",
                        "help": "A file path relative to the project root",
                        "positional": True,
                        "required": True,
                    }
                ],
            },
            "_browse-index": {
                "help": "Opens a project subfolder's index.html file",
                "ref": "_browse-file ${_folder}/index.html",
                "args": [
                    {
                        "name": "_folder",
                        "help": "A folder path relative to the project root",
                        "positional": True,
                        "required": True,
                    }
                ],
            },
            "_delete": {
                "help": "Deletes a project file",
                "expr": "pathlib.Path(_file).unlink() if pathlib.Path(_file).exists() else None",
                "imports": ["pathlib"],
                "args": [
                    {
                        "name": "_file",
                        "help": "A file path relative to the project root",
                        "positional": True,
                        "required": True,
                    }
                ],
            },
            "_rmtree": {
                "help": "Deletes a project subfolder and its contents",
                "expr": "shutil.rmtree(_folder) if pathlib.Path(_folder).exists() else None",
                "imports": ["shutil", "pathlib"],
                "args": [
                    {
                        "name": "_folder",
                        "help": "A folder path relative to the project root",
                        "positional": True,
                        "required": True,
                    }
                ],
            },
        },
    }


def test_default(schema):
    assert tasks() == schema


def test_exclude_tasks(schema):
    output = tasks(exclude_tasks=("audit", "sync", "upgrade"))
    groups = schema["groups"]
    del groups["200_env"]
    del groups["300_security"]
    assert output == schema


def test_include_tasks(schema):
    output = tasks(include_tasks=("audit", "sync", "upgrade"))
    groups = schema["groups"]
    schema["groups"] = {key: groups[key] for key in ["200_env", "300_security"]}
    assert output == schema


def test_exclude_groups(schema):
    output = tasks(exclude_groups=("env", "security"))
    groups = schema["groups"]
    del groups["200_env"]
    del groups["300_security"]
    assert output == schema


def test_include_groups(schema):
    output = tasks(include_groups=("security", "env"))
    groups = schema["groups"]
    schema["groups"] = {key: groups[key] for key in ["200_env", "300_security"]}
    assert output == schema


# def test_surgical_include(schema):
#     output = tasks(exclude_groups=("env", "security"), include_tasks=("sync"))
#     groups = schema["groups"]
#     del groups["300_security"]
#     del groups["200_env"]['tasks']["upgrade"]
#     assert output == schema


def test_surgical_exclude(schema):
    output = tasks(include_groups=("env", "security"), exclude_tasks=("sync"))
    groups = schema["groups"]
    schema["groups"] = {key: groups[key] for key in ["200_env", "300_security"]}
    del schema["groups"]["200_env"]["tasks"]["sync"]
    assert output == schema
