Running Tasks
=============

.. important::

    You will not be able to run tasks until you have :doc:`configured pyproject.toml <pyproject>`.


Basic Usage
-----------

In general, you can invoke a task by calling::

    poe <task-name>

from a project's root folder. For example::

    cd path/to/my/project

    poe audit
    poe lint
    poe tests

Most tasks should actually work anywhere within a project folder::

    cd tests

    # Still works, and lints everything (not just the tests)
    poe lint

but the root folder is usually best. In particular, we strongly recommend the root
folder for any tasks running in a CI/CD pipeline.


Setup Task
----------
The :ref:`setup task <task.setup>` is a special case, as it is typically run *before*
any developer dependencies are installed (included ``poe-tasks-common`` itself). To
accommodate this, we recommend using `uvx`_ to run the command from the project root::

    cd path/to/my/project
    uvx --from poethepoet poe setup

.. _uvx: https://docs.astral.sh/uv/concepts/tools/

.. important::

    This syntax assumes you have already `installed uv <https://docs.astral.sh/uv/getting-started/installation/>`_.


Help Text
---------
You can use the ``poe`` command to display help text documenting all the command-line
tasks that are available for a project::

    poe

.. dropdown:: Show Help Text

    .. code:: output

        Poe the Poet

        Usage:
        poe [global options] task [task arguments]

        Global options:
        -h, --help [TASK]     Show this help page and exit, optionally supply a task.
        --version             Print the version and exit
        -v, --verbose         Increase output (repeatable)
        -q, --quiet           Decrease output (repeatable)
        -d, --dry-run         Print the task contents but don't actually run it
        -C, --directory PATH  Specify where to find the pyproject.toml
        -e, --executor EXECUTOR
                                Override the default task executor
        -X, --executor-opt KEY[=VALUE]
                                Set executor configuration for this run.
        --ansi                Force enable ANSI output
        --no-ansi             Force disable ANSI output

        Configured tasks:
        Setup:
        setup                 Syncs all dependencies and installs pre-commit
        install-precommit     Installs pre-commit

        Environment:
        sync                  Syncs the development environment
        upgrade               Syncs and upgrades the development environment

        Security:
        audit                 Check package dependencies for security issues

        Linting:
        format                Formats the code and its tests
        lint                  Lints the code and its tests

        Testing:
        tests                 Runs the tests and requires a minimum coverage
            --min-coverage      Minimum required test coverage percent [default: ${MIN_COVERAGE:-100}]
        htmlcov               Builds an HTML coverage report and opens in a web browser
        coverage              Prints the coverage report for the tests

        Documentation:
        docs                  Rebuilds the documentation
            -o, --output        Folder containing the built documentation [default: ${DOCS_OUTPUT:-public}]
        open-docs             Opens the built documentation in a web browser
            -o, --output        Folder containing the built documentation [default: ${DOCS_OUTPUT:-public}]


You can also print help text for a specific task by using ``poe --help <task>``.
For example::

    poe --help tests

.. code:: output

    Description:
    Runs the tests and requires a minimum coverage

    Usage:
    poe [global options] tests [named arguments] -- [free arguments]

    Named arguments:
    --min-coverage      Minimum required test coverage percent [default: ${MIN_COVERAGE:-100}]


Reference Tasks
---------------
You can also invoke tasks within other tasks using references.
This is typically done in a new task's definition within a ``pyproject.toml`` file.
For example::

    [tool.poe.tasks.build-and-open-docs]
    help = "Builds and opens the docs"
    default_item_type = "ref"
    sequence = ["docs", "open-docs"]

This is discussed in greater detail in the :doc:`extending tasks </extending/index>` section.
You can also learn more about references in poethepoet's
`reference task guide <https://poethepoet.natn.io/tasks/task_types/ref.html>`_.
Note that :ref:`utility tasks` can **only** be run as references. They are not available
from the command line.

For example, this would work (in ``pyproject.toml``)::

    [tool.poe.tasks.open-website]
    help = "Opens the project website"
    ref = "_browse https://my-project-website.com"

But this would not (command line)::

    poe _browse https://my-project-website.com
