Task Overview
=============

This page introduces all the tasks available from ``poe-tasks-common``.
For more details, refer to the :doc:`Task API </api/tasks>`.

.. _standard tasks:

Standard Tasks
--------------
The following table describes all standard tasks. These tasks can all be invoked from
the command line.

.. list-table::
    :header-rows: 1

    * - Task
      - Description
      - Dependencies
    * -
      -
      -
    * - **Setup**
      -
      -
    * - :ref:`setup <task.setup>`
      - Installs all project dependencies. Also installs a pre-commit hook for the project.
      - `uv`_, `pre-commit`_
    * - :ref:`install-precommit <task.install-precommit>`
      - Install a pre-commit hook for the project.
      - `uv`_, `pre-commit`_
    * -
      -
      -
    * - **Environment**
      -
      -
    * - :ref:`sync <task.sync>`
      - Syncs the development environment with all listed dependencies.
      - `uv`_
    * - :ref:`upgrade <task.upgrade>`
      - Upgrades all dependencies (within allowed constraints) and re-syncs the development environment.
      - `uv`_
    * -
      -
      -
    * - **Security**
      -
      -
    * - :ref:`audit <task.audit>`
      - Check dependencies for security vulnerabilities.
      - `pip-audit`_
    * -
      -
      -
    * - **Linting**
      -
      -
    * - :ref:`lint <task.lint>`
      - Lints the code and its tests.
      - `ruff`_
    * - :ref:`format <task.format>`
      - Formats the code and its tests.
      - `ruff`_
    * -
      -
      -
    * - **Testing**
      -
      -
    * - :ref:`tests <task.tests>`
      - Runs the tests, prints a coverage report, and requires a minimum test coverage.
      - `pytest`_, `coverage`_, `pytest-cov`_
    * - :ref:`coverage <task.coverage>`
      - Prints a coverage report.
      - `coverage`_
    * - :ref:`htmlcov <task.htmlcov>`
      - Builds an HTML coverage report and opens it in a web browser.
      - `coverage`_
    * -
      -
      -
    * - **Documentation**
      -
      -
    * - :ref:`docs <task.docs>`
      - Builds the documentation (deleting any pre-existing builds).
      - `sphinx`_
    * - :ref:`open-docs <task.open-docs>`
      - Opens the built documentation in a web browser.
      - None


.. _utility tasks:

Utility Tasks
-------------
The package also includes utility tasks that advanced users can use as building blocks
for more complex workflows. Note that these utility tasks are only available as
`reference tasks`_ - they cannot be invoked directly from the command line.

.. _reference tasks: https://poethepoet.natn.io/tasks/task_types/ref.html

.. list-table::
    :header-rows: 1

    * - Task
      - Description
    * -
      -
    * - **Deletion**
      -
    * - :ref:`_rmtree <task._rmtree>`
      - Deletes a project folder and all of its contents.
    * - :ref:`_delete <task._delete>`
      - Deletes a project file.
    * -
      -
    * - **Browse**
      -
    * - :ref:`_browse <task._browse>`
      - Opens a URL or file URI in a web browser.
    * - :ref:`_browse-file <task._browse-file>`
      - Opens a project file in a web browser.
    * - :ref:`_browse-index <task._browse-index>`
      - Opens a project folder's ``index.html`` file in a web browser.
