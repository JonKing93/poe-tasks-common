Ordering Groups
===============

When you call ``poe help``, poe will display help text that records all public tasks
that can be called from the command line. The ``poe-tasks-common`` package uses task
groups to collect related tasks, and these groups are ordered via an integer-based
numbering scheme. This scheme ensures that groups render in workflow order in the
help text, rather than in a strictly alphabetical order.

More specifically, the ordering scheme prepends a hundreds-based integer to each
group name in the :doc:`task schema <schema>`. As follows:

.. list-table::
    :header-rows: 1

    * - Group
      - Schema Name
    * - Setup
      - ``100_setup``
    * - Environment
      - ``200_env``
    * - Security
      - ``300_security``
    * - Linting
      - ``400_lint``
    * - Testing
      - ``500_test``
    * - Documentation
      - ``600_docs``


Adding New Groups
-----------------
If you plan to write a new task group, you can use the numbering scheme to ensure that
the new group's help text renders in the correct location. For example, say you have a new
group that should appear between the linting and testing groups. You can implement this
using something like::

    [tool.poe.groups.450_my-group]
    ...

In general, groups will render in numeric order, so if you have multiple new groups,
you can use something like::

    [tool.poe.groups.425_my-group-A]
    # Group A should render first
    ...

    [tool.poe.groups.450_my-group-B]
    # Group B should render second
    ...

    [too.poe.groups.475_my-group-C]
    # Group C will render third
    ...



Changing the Default Order
--------------------------
You can change the default ordering by altering the integer in a group's name in the
:doc:`task schema <schema>`.
For example, say you want to move the security group between the setup and environment
groups. You could do this using::

    from poe_tasks_common import tasks

    schema = tasks()
    security = schema['groups'].pop('300_security')
    schema['groups']['150_security'] = security
