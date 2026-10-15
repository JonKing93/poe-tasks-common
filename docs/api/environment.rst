Environment Variables
=====================

Certain tasks in ``poe-tasks-common`` can be configured using environment variables.
We recommend :doc:`setting these in pyproject.toml </guide/pyproject>`, but they can also be configured
at the host OS level.

.. envvar:: MIN_COVERAGE

    **DEFAULT:** 100%

    The minimum required test coverage for the :ref:`tests <task.tests>` task.

    Example::

        [tool.poe]
        MIN_COVERAGE = 85


.. envvar:: DOCS_OUTPUT

    **DEFAULT:** ``public``

    The folder in which built documentation is saved. Used by the :ref:`docs <task.docs>` and :ref:`open-docs <task.open-docs>` tasks.

    Example::

        [tool.poe]
        DOCS_OUTPUT = "pages"
