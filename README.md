# poe-tasks-common

[![Documentation](https://img.shields.io/badge/Documentation-Click%20Here!-blue)](https://poe-tasks-common.readthedocs.io)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/downloads)
[![PyPI](https://img.shields.io/pypi/v/poe-tasks-common.svg?color=green)](https://pypi.org/project/poe-tasks-common/)
[![Build Status](https://github.com/JonKing93/poe-tasks-common/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/JonKing93/poe-tasks-common/actions/workflows/build.yml?query=branch%3Amain)
[![Coverage](https://coveralls.io/repos/github/JonKing93/poe-tasks-common/badge.svg?branch=main)](https://coveralls.io/github/JonKing93/poe-tasks-common?branch=main)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/license/mit)

An opinionated collection of common poe tasks

## About

The [poe](https://poethepoet.natn.io/index.html) task runner allows developers to create commands that run repeated tasks for software development. Common examples include commands for formatting the code, running the tests, and building the documentation. The `poe-tasks-common` package provides a pre-configured collection of these tasks. By adding `poe-tasks-common` to your `pyproject.toml` file, you gain immediate access to core environment, security, linting, testing, and documentation commands, without needing to learn to build poe tasks.

## Examples

By adding `poe-tasks-common` to a `pyproject.toml` file, you gain immediate access to commands like:

```
# Checks for security vulnerabilities
poe audit

# Formats the code and tests
poe format

# Lints the code and tests
poe lint

# Runs the tests, requires a certain coverage.
# Opens coverage report in a web browser.
poe tests
poe htmlcov

# Builds the docs. Opens docs in a web browser
poe docs
poe open-docs
```

## Opinionated Toolset

As stated, `poe-tasks-common` is an opinionated collection - the tasks it provides are intended for specific developer tools like [pytest](https://docs.pytest.org/en/stable/), [ruff](https://docs.astral.sh/ruff/), [pip-audit](https://pypi.org/project/pip-audit/) and others. We are not claiming that these tools are the absolute best choices for every possible use case. Rather, this toolset is intended as a common core suitable for many projects. We also emphasize that `poe-tasks-common` provides options for filtering out unwanted tools and tasks.

## When to use poe-tasks-common

Use `poe-tasks-common` when you want to quickly start developing a project, without needing to configure poe commands. The package is also useful when you want a common core of commands that you can use across multiple projects. Finally, advanced users may find the package a useful building block for more complex poe frameworks.
