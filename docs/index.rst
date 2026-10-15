poe-tasks-common
================

.. image:: https://img.shields.io/badge/Python-3.11+-blue
    :alt: Python
    :target: https://www.python.org/downloads
.. image:: https://img.shields.io/pypi/v/poe-tasks-common.svg?color=green
    :alt: PyPI
    :target: https://pypi.org/project/poe-tasks-common
.. image:: https://github.com/JonKing93/poe-tasks-common/actions/workflows/build.yml/badge.svg?branch%3Amain
    :alt: Build Status
    :target: https://github.com/JonKing93/poe-tasks-common/actions/workflows/build.yml?query=branch%3Amain
.. image:: https://coveralls.io/repos/github/JonKing93/poe-tasks-common/badge.svg?branch=main
    :alt: Coverage
    :target: https://coveralls.io/github/JonKing93/poe-tasks-common?branch=main
.. image:: https://img.shields.io/badge/License-MIT-blue
    :alt: License
    :target: https://opensource.org/license/mit

A pre-configured, opinionated collection of common `poe`_ tasks.


About
-----
The `poe`_ task runner allows developers to create commands that run repeated tasks for
software development. Common examples include commands for formatting the code,
running the tests, and building the documentation. The ``poe-tasks-common`` package
provides a pre-configured collection of these tasks. By adding ``poe-tasks-common`` to
your ``pyproject.toml`` file, you gain immediate access to core environment, security,
linting, testing, and documentation commands, without needing to learn to build
poe tasks.


Examples
--------

By adding poe-tasks-common to a ``pyproject.toml`` file, you gain immediate access to
commands like::

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


Opinionated Toolset
-------------------
As stated, ``poe-tasks-common`` is an opinionated collection - the tasks it provides are
intended for specific developer tools like `pytest`_, `ruff`_, `pip-audit`_ and others.
We are not claiming that these tools are the absolute best choices for every possible use case.
Rather, this toolset is intended as a common core suitable for many projects.
We also emphasize that ``poe-tasks-common`` provides options for filtering out
unwanted tools and tasks. The default tasks are built around the following tools:

.. list-table::
    :header-rows: 1

    * - Topic
      - Tools
    * - Project Management
      - `uv`_
    * - Tooling
      - `poethepoet`_
    * - Hooks
      - `pre-commit`_
    * - Security
      - `pip-audit`_
    * - Linting / Formatting
      - `ruff`_
    * - Testing
      - `pytest`_, `coverage`_, `pytest-cov`_
    * - Documentation
      - `sphinx`_


Why use poe-tasks-common?
-------------------------
Use ``poe-tasks-common`` when you want to quickly start developing a project, without
needing to configure poe commands. The package is also useful when you want a common
core of commands that you can use across multiple projects. Finally, advanced users may
find the package a useful building block for more complex poe frameworks.


Using these docs
----------------
The :doc:`User Guide </guide/index>` is designed to introduce new users to the package
and is usually the best place to start. By the end of the guide, you should be able to
use ``poe-tasks-common`` to help develop a project. The
:doc:`Extending Tasks </extending/index>` section discusses how developers can build
off of the ``poe-tasks-common`` framework, and the :doc:`API </api/index>` provides the
complete reference guide to the package.



.. toctree::
    :caption: Usage
    :hidden:

    Introduction <self>
    Installation <install>
    User Guide </guide/index>
    Extending Tasks </extending/index>
    API </api/index>


.. toctree::
    :caption: Resources
    :hidden:

    Contributing </resources/contributing>
    Release Notes </resources/release-notes>
    License </resources/license>
    Github Repository <https://github.com/JonKing93/poe-tasks-common>
    PyPI <https://pypi.org/project/poe-tasks-common/>
