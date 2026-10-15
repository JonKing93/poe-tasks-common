"""
Function that collects and returns the complete poe schema
"""

from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

from poe_tasks_common._groups import GROUPS
from poe_tasks_common._utilities import TASKS as UTILITIES

if TYPE_CHECKING:
    Strings = list[str] | tuple[str, ...]


def tasks(
    *,
    exclude_tasks: Strings = (),
    include_tasks: Strings = (),
    exclude_groups: Strings = (),
    include_groups: Strings = (),
) -> dict:
    """
    Builds, filters, and exports a task schema

    tasks()
    Builds and returns the complete task schema dict.

    tasks(*, exclude_tasks)
    tasks(*, include_tasks)
    tasks(*, exclude_groups)
    tasks(*, include_groups)
    Returns a filtered schema dict. Use these options to select which tasks are
    included in the final schema. Use `include_tasks` or `exclude_tasks` to filter
    by specific task names. Use `include_groups` or `exclude_groups` to filter by
    task groups. Each provided filter should be a sequence of strings. When multiple
    filters are provided, they are have the following priority:

        exclude_tasks > include_tasks > exclude_groups > include_groups

    In brief, task filters take priority over group filters, and excludes have priority
    over includes. Note that providing an "include" filter activates opt-in
    behavior - only the included tasks are exported, all others are discarded.

    Args:
        exclude_tasks: Specific tasks that should be excluded from the schema
        include_tasks: Specific tasks that should be included in the schema
        exclude_groups: Task groups that should be excluded from the schema
        include_groups: Tasks groups that should be included in the schema

    Returns:
        dict: The poe task schema
    """

    filtered_groups = _filter(
        GROUPS, include_tasks, exclude_tasks, include_groups, exclude_groups
    )
    return {
        "tasks": deepcopy(UTILITIES),
        "groups": deepcopy(filtered_groups),
    }


def _filter(
    all_groups: dict,
    include_tasks: Strings,
    exclude_tasks: Strings,
    include_groups: Strings,
    exclude_groups: Strings,
):
    "Additively builds a filtered group dict"

    # Determine whether tasks are opt-in or opt-out.
    # Default is opt-out. Opt-in is triggered if an inclusion group is provided
    is_opt_out = not (include_tasks or include_groups)

    # Check baseline group eligibility
    groups = {}
    for group_name, group in all_groups.items():
        group_id = group_name.split("_", maxsplit=1)[1]
        keep_group = (
            is_opt_out or group_id in include_groups or group_name in include_groups
        )
        if group_id in exclude_groups or group_name in exclude_groups:
            keep_group = False

        # Determine the eligibility of tasks within the group
        tasks = {}
        for task_name, task in group["tasks"].items():
            keep_task = keep_group
            if task_name in include_tasks:
                keep_task = True
            if task_name in exclude_tasks:
                keep_task = False

            # Save any tasks that are eligible
            if keep_task:
                tasks[task_name] = task

        # Only save groups that have tasks
        if tasks:
            groups[group_name] = {"heading": group["heading"], "tasks": tasks}
    return groups
