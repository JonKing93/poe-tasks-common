Configuring ``pyproject.toml``
==============================

We recommend most users install and configure poe-tasks-common via their project's
``pyproject.toml`` file. If you are not familiar with these files, they define a Python
project, and are a standard place for managing developer tools. If you
want to learn more, there are many resources online - we recommend the following two
guides:

* `RealPython Guide <https://realpython.com/python-pyproject-toml/>`_
* `PyPA Guide <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>`_


.. _basic configuration:

Basic Configuration
-------------------
This configuration is a good starting point for most projects.
It contains a core set of developer tools and ensures that all the tasks in ``poe-tasks-common`` can run.
Add the following lines to ``pyproject.toml``::

    [dependency-groups]
    tooling = ["poethepoet==0.48.0", "poe-tasks-common"]
    hooks = ["pre-commit"]
    security = ["pip-audit"]
    lint = ["ruff"]
    test = ["pytest", "coverage", "pytest-cov"]
    docs = ["sphinx"]

.. tip::

    We recommend pinning ``poethepoet`` to an explicit version to prevent poe from
    attempting to modify itself when updating development environments. We've used
    version ``0.48.0`` in this example, but we recommend whichever version is most recent.

.. caution::

    DO NOT include ``uv`` in your dependency groups, as `uv`_ is managed outside the project.

----

Next, register poe-tasks-common with poe::

    [tool.poe]
    include_script = "poe_tasks_common:tasks"
    executor = "uv"

.. note::

    If you are not using `uv`_, remove the ``executor`` line from the previous block.

----

Finally, sync your development environment. The built-in setup task can do this for you::

    cd path/to/my/project
    uvx --from poethepoet poe setup

Alternatively, if you prefer to use `uv`_ directly::

    cd path/to/my/project
    uv sync --all-groups

That's it, you're ready to go! Head over to the :doc:`Running Tasks Guide <running-tasks>`
to learn how to run the provided tasks.


Additional Tools
----------------

The :ref:`basic configuration` is a good starting point, but many users will need additional developer
tools to manage their project. As such, you can modify any of the dependency groups to
include additional libraries. For example, to use additional libraries to build the docs,
you could use something like::

    [dependency-groups]
    docs = ["sphinx", "furo", "sphinx-design", "sphinx-copybutton"]
    ...

You can also add new groups altogether. For example, adding a new group with tools for
publishing releases::

    [dependency-groups]
    publish = ["twine"]
    ...


Using Different Tools
---------------------
As previously stated, ``poe-tasks-common`` is an opinionated collection. By default, it assumes you want to
use `pip-audit`_, `ruff`_, `pytest`_, `sphinx`_, etc. But if you want to use different
development tools, you can always change any of the dependency groups to your preferred tool set.
However, note that the associated tasks from ``poe-tasks-common``
will no longer work if you remove tools from :ref:`basic configuration`.

For example, to use different linting tools, you could use::

    [dependency-groups]
    lint = ["black", "isort"]
    ...

In this case, the tasks in the poe-tasks-common :ref:`linting group <group.linting>` (``poe lint`` and ``poe format``)
will no longer work. But the remaining tasks (security, testing, docs, etc) will all still work.

When using different tools, we recommend configuring your installation to
:doc:`filter out broken tasks <filtering>`. Otherwise, the broken tasks are still exposed
to your project (they just return an error). Refer to the :doc:`filtering guide <filtering>` for more details.


Configuring Specific Tasks
--------------------------
Some tasks (:ref:`tests <task.tests>`, :ref:`docs <task.docs>`, and :ref:`open-docs <task.open-docs>`) have configurable behavior.
For example, you can configure the minimum required test coverage (for :ref:`tests <task.tests>`),
and the output folder for built documentation (:ref:`docs <task.docs>` and :ref:`open-docs <task.open-docs>`).
In general, you can configure a value by adding a recognized key to the ``tool.poe``
block in ``pyproject.toml``.

Use :envvar:`MIN_COVERAGE` to set the minimum required test coverage (default: 100%).
For example, to change the minimum required coverage to 85%, use::

    [tool.poe]
    MIN_COVERAGE = 85
    ...

Use :envvar:`DOCS_OUTPUT` to set the output folder of built documentation (default: ``public``).
For example, to change the output folder to ``pages`` use::

    [tool.poe]
    DOCS_OUTPUT = "pages"
    ...


.. _pyproject.toml: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
