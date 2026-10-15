Filtering Tasks
===============
The ``poe-tasks-common`` package provides several options for filtering which tasks are
exposed to your project. In order of decreasing priority:

.. list-table::
    :header-rows: 1

    * - Option
      - Description
    * - ``exclude_tasks``
      - Specific tasks that should not be exposed to the project,
    * - ``include_tasks``
      - Specific tasks that should be exposed to the project.
    * - ``exclude_groups``
      - Task groups that should not be exposed to the project.
    * - ``include_groups``
      - Tasks groups that should be exposed to the project.

These filters are often used to remove certain tasks from your installation.

TODO - Add more info here.
