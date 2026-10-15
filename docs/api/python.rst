Python API
==========

.. highlight:: python

.. py:module:: poe_tasks_common

.. py:function:: tasks(*, exclude_tasks=(), include_tasks=(), exclude_groups=(), include_groups=())

    Builds, filters, and exports a task schema

    ::

        tasks()

    Builds and returns the complete task schema dict.

    ::

        tasks(*, exclude_tasks)
        tasks(*, include_tasks)
        tasks(*, exclude_groups)
        tasks(*, include_groups)

    Returns a filtered schema dict. Use these options to select which tasks are
    included in the final schema. Use ``include_tasks`` or ``exclude_tasks`` to filter
    by specific task names. Use ``include_groups`` or ``exclude_groups`` to filter by
    task groups. Each provided filter should be a sequence of strings. When multiple
    filters are provided, they are have the following priority:

    ``exclude_tasks > include_tasks > exclude_groups > include_groups``

    In brief, task filters take priority over group filters, and excludes have priority
    over includes. Note that providing an "include" filter activates opt-in
    behavior - only the included tasks are exported, all others are discarded.

    :Args:
        * **exclude_tasks** (*list[str]*) -- Specific tasks that should be excluded from the schema
        * **include_tasks** (*list[str]*) -- Specific tasks that should be included in the schema
        * **exclude_groups** (*list[str]*) -- Task groups that should be excluded from the schema
        * **include_groups** (*list[str]*) -- Tasks groups that should be included in the schema

    :Returns:
        *dict* -- The poe task schema
