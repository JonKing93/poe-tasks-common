User Guide
==========
This user guide is designed to introduce new users to the package. It discusses the
tasks included in the package, how to invoke tasks, and how to configure tasks via
``pyproject.toml``. This user guide should be sufficient for many users, but if you
want to build new tasks off the ``poe-tasks-common`` framework, refer to the
:doc:`extending tasks </extending/index>` section instead.

----

:doc:`Tasks Overview <tasks>`
    Provides a summary of all the tasks included in the package.

:doc:`How to Run Tasks <running-tasks>`
    How to run tasks from the command line and within other tasks.

:doc:`Configuring pyproject.toml <pyproject>`
    How to configure ``pyproject.toml`` to use tasks from ``poe-tasks-common``.

:doc:`Filtering Tasks <filtering>`
    Advanced configuration options for users who only want to install specific tasks.


.. toctree::
    :hidden:

    Tasks Overview <tasks>
    How to run tasks <running-tasks>
    Configure pyproject.toml <pyproject>
    Filtering Tasks <filtering>
