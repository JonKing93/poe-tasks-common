Tasks
=====
The complete reference guide to available tasks and task groups.


.. _group.setup:

Setup
-----
Task group for one time setup tasks.

Group definition::

    [tool.poe.groups.100_setup]
    heading = "Setup:"

----

.. _task.setup:

``poe setup``
+++++++++++++

.. program:: poe setup

Uses `uv`_ to build the development environment and install `pre-commit`_.
Calls the :ref:`sync <task.sync>` and :ref:`install-precommit <task.install-precommit>` tasks.

.. tip::

    This command is often invoked via `uvx <https://docs.astral.sh/uv/guides/tools/#running-tools>`_,
    as this will allow the command to install poe itself::

        uvx --from poethepoet poe setup

Task definition::

    [tool.poe.groups.100_setup.tasks.setup]
    help = "Syncs all dependencies and installs pre-commit"
    default_item_type = "ref"
    sequence = [
        "sync --frozen",
        "install-precommit",
    ]

----

.. _task.install-precommit:

``poe install-precommit``
+++++++++++++++++++++++++

.. program:: poe install-precommit

Uses `uv`_ to install `pre-commit`_, thereby enabling pre-commit hooks.

Task definition::

    [tool.poe.groups.100_setup.tasks.install-precommit]
    help = "Installs pre-commit"
    default_item_type = "cmd"
    sequence = [
        "uv tool install pre-commit --with pre-commit-uv --force-reinstall",
        "pre-commit install",
    ]


.. _group.env:

Environment
-----------
Task group for managing the development environment.

Group definition::

    [tool.poe.groups.200_env]
    heading = "Environment:"

----

.. _task.sync:

``poe sync``
++++++++++++

.. program:: poe sync

Uses `uv`_ to sync the development environment.

Task definition::

    [tool.poe.groups.200_env.tasks.sync]
    help = "Syncs the development environment"
    cmd = "uv sync --all-groups --all-extras"

----

.. _task.upgrade:

``poe upgrade``
+++++++++++++++
.. program:: poe upgrade

Uses `uv`_ to upgrade all dependencies and re-sync the development environment.
Calls the :ref:`sync <task.sync>` task.

Task definition::

    [tool.poe.groups.200_env.tasks.upgrade]
    help = "Syncs and upgrades the development environment"
    ref = "sync --uprade"


.. _group.security:

Security
--------
Task group for security testing.

Group definition::

    [tool.poe.groups.300_security]
    heading = "Security:"


----

.. _task.audit:

``poe audit``
+++++++++++++
.. program:: poe audit

Uses `pip-audit`_ to check dependencies for security issues.

Note that any additional command line options are forwarded directly to ``pip-audit``.
This can be useful for ignoring specific vulnerabilities. For example::

    poe audit --ignore-vuln PYSEC-abc123

Task definition::

    [tool.poe.groups.300_security.tasks.audit]
    help = "Check package dependencies for security issues"
    cmd = "pip-audit"


.. _group.linting:

Linting
-------
Task group for linting and formatting.

Group definition::

    [tool.poe.groups.400_lint]
    heading = "Linting:"

----

.. _task.lint:

``poe lint``
++++++++++++
.. program:: poe lint

Uses `ruff`_ to lint the code and its tests.

Task definition::

    [tool.poe.groups.400_lint.tasks.lint]
    help = "Lints the code and its tests"
    cmd = "ruff check src tests"

----

.. _task.format:

``poe format``
++++++++++++++
.. program:: poe format

Uses `ruff`_ to format the code and its tests.
Note that this is functionally equivalent to running `black`_ and `isort`_.

Task definition::

    [tool.poe.groups.400_lint.tasks.format]
    help = "Formats the code and its tests"
    default_item_type = "cmd"
    sequence = [
        "ruff format src tests",
        "ruff check src tests --select I --fix",
    ]


.. _group.test:

Testing
-------
Task group to facilitate testing.

Group definition::

    [tool.poe.groups.500_test]
    heading = "Testing:"

----

.. _task.tests:

``poe tests``
+++++++++++++
.. program:: poe tests --min-coverage

Uses `pytest`_ to run the tests. Prints a coverage report, and requires a minimum test coverage.
Calls the :ref:`coverage <task.coverage>` task::

    # Run with default coverage requirement
    poe tests

    # Override the minimum test coverage
    poe tests --min-coverage 85

.. option:: --min-coverage

    The minimum required test coverage. Defaults to the value configured by :envvar:`MIN_COVERAGE`,
    or to 100% if no value is configured.

Task definition::

    [tool.poe.groups.500_test.tasks.tests]
    help = "Runs the tests and requires a minimum coverage"
    sequence = [
        { cmd = "pytest tests --cov=src --cov=/tests --cov-fail-under=${_min_coverage} --cov-report xml:coverage.xml" },
        { ref = "coverage" },
    ]

        [[tool.poe.groups.500_test.tasks.tests.args]]
        name = "_min_coverage"
        help = "Minimum required test coverage percent"
        options = ["--min-coverage"]
        default = "${MIN_COVERAGE:-100}"

----

.. _task.coverage:

``poe coverage``
++++++++++++++++
.. program:: poe coverage

Prints a coverage report.

Task definition::

    [tool.poe.groups.500_test.tasks.coverage]
    help = "Prints the coverage report for the tests"
    cmd = "coverage report"

----

.. _task.htmlcov:

``poe htmlcov``
+++++++++++++++
.. program:: poe htmlcov

Builds an HTML coverage report and opens it in a web browser.
Calls the :ref:`_rmtree <task._rmtree>` and :ref:`_browse-index <task._browse-index>` tasks.

Task definition::

    [tool.poe.groups.500_test.tasks.coverage]
    help =  "Builds an HTML coverage report and opens in a web browser"
    sequence = [
        { ref = "_rmtree htmlcov" },
        { cmd = "coverage html --skip-covered" },
        { ref = "_browse-index htmlcov" },
    ]


.. _group.docs:

Documentation
-------------
Task group to facilitate building the documentation.

Group definition::

    [tool.poe.groups.600_docs]
    heading = "Documentation:"

----

.. _task.docs:

``poe docs``
++++++++++++
.. program:: docs

Deletes any existing documentation build, then rebuilds the documentation.
Calls the :ref:`_rmtree <task._rmtree>` task.

.. option:: -o, --output

    The folder in which the built documentation should be saved.
    Defaults to the value configured by :envvar:`DOCS_OUTPUT`,
    or to ``public`` if no value is configured.

Task definition::

    [tool.poe.groups.600_docs.tasks.docs]
    help = "Rebuilds the documentation"
    sequence = [
        { ref = "_rmtree ${_output_folder}" },
        { cmd = "sphinx-build -qa docs ${_output_folder}" },
    ]

        [[tool.poe.groups.600_docs.tasks.docs.args]]
        name = "_output_folder"
        help = "Folder containing the built documentation"
        options = ["-o", "--output"]
        default = "${DOCS_OUTPUT:-public}"

----

.. _task.open-docs:

``poe open-docs``
+++++++++++++++++
.. program:: open-docs

Opens the built documentation in a web browser.
Calls the :ref:`_browse-index <task._browse-index>` task.

.. option:: -o, --output

    The folder holding the built documentation.
    Defaults to the value configured by :envvar:`DOCS_OUTPUT`,
    or to ``public`` if no value is configured.

Task definition::

    [tool.poe.groups.600_docs.tasks.open-docs]
    help = "Opens the built documentation in a web browser"
    ref = "_browse-index ${_output_folder}"

        [[tool.poe.groups.600_docs.tasks.open-docs.args]]
        name = "_output_folder"
        help = "Folder containing the built documentation"
        options = ["-o", "--output"]
        default = "${DOCS_OUTPUT:-public}"


.. _group.delete:

Utilities: Deletion
-------------------
Utility tasks for deleting files.

.. _task._rmtree:

``_rmtree``
+++++++++++
.. program:: _rmtree

Deletes a project subfolder and its contents.

Usage: ``_rmtree FOLDER``

.. option:: FOLDER

    The project subfolder that should be deleted.
    Should be a folder path relative to the project folder.

Example usage::

    [tool.poe.tasks.my-task]
    ref = "_rmtree my-subfolder"

Task definition::

    [tool.poe.tasks._rmtree]
    help = "Deletes a project subfolder and its contents"
    expr = "shutil.rmtree(_folder) if pathlib.Path(_folder).exists() else None"
    imports = ["shutil", "pathlib"]

        [[tool.poe.tasks._rmtree.args]]
        name = "_folder"
        help = "A folder path relative to the project root"
        positional = true
        required = true

----

.. _task._delete:

``_delete``
+++++++++++
.. program:: _delete

Deletes a project file.

Usage: ``_delete FILE``

.. option:: FILE

    The project file that should be deleted.
    Should be a path relative to the project folder.

Example usage::

    [tool.poe.tasks.my-task]
    ref = "_delete scratch/file.txt"

Task definition::

    [tool.poe.tasks._rmtree]
    help = "Deletes a project file"
    expr = "pathlib.Path(_file).unlink() if pathlib.Path(_file).exists() else None"
    imports = ["pathlib"]

        [[tool.poe.tasks._delete.args]]
        name = "_file"
        help = "A file path relative to the project root"
        positional = true
        required = true


.. _group.browse:

Utilities: Browse
-----------------
Utility tasks for opening files in a web browser.

.. _task._browse:

``_browse``
+++++++++++
.. program:: _browse

Opens a URL or file URI in a web browser.

Usage: ``_browse URI``

.. option:: URI

    The web URL or file URI that should be opened.

Example usage::

    [tool.poe.tasks.my-task-1]
    ref = "_browse https://www.example.com"

    [tool.poe.tasks.my-task-2]
    ref = "_browse file:///path/to/project/file.html"

Task definition::

    [tool.poe.tasks._browse]
    help = "Opens a URI (file or web URL) in a web browser"
    expr = "webbrowser.open(_uri)"
    imports = ["webbrowser"]

        [[tool.poe.tasks._browse.args]]
        name = "_uri"
        help = "The target URI (file or web URL) to open"
        positional = true
        required = true

----

.. _task._browse-file:

``_browse-file``
++++++++++++++++
.. program:: _browse-file

Opens a project file in a web browser.

Usage: ``_browse-file FILE``

.. option:: FILE

    The project file to open in a web browser.
    Should be a path relative to the project folder.

Example usage::

    [tool.poe.tasks.my-task]
    ref = "_browse-file pages/index.html"

Task definition::

    [tool.poe.tasks._browse-file]
    help = "Opens a project file in a web browser"
    expr = "webbrowser.open( pathlib.Path(_path).resolve().as_uri() )"
    imports = ["webbrowser", "pathlib"]

        [[tool.poe.tasks._browse-file.args]]
        name = "_path"
        help = "A file path relative to the project root"
        required = true
        positional = true

----

.. _task._browse-index:

``_browse-index``
+++++++++++++++++
Opens an index.html file from a project subfolder in a web browser.

Usage: ``_browse-index FOLDER``

.. option:: FOLDER

    The project subfolder whose index.html file should be opened in a web browser.
    Should be a path relative to the project folder.

Example usage::

    [tool.poe.tasks.my-task]
    ref = "_browse-index pages"

Task definition::

    [tool.poe.tasks._browse-index]
    help = "Opens a project subfolder's index.html file in a web browser"
    ref = "_browse-file ${_folder}/index.html"

        [[tool.poe.tasks._browse-index.args]]
        name = "_folder"
        help = "A folder path relative to the project root"
        positional = true
        required = true
