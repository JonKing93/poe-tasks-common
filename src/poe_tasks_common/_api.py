"""
Function that collects and returns all the task groups
"""

from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

from poe_tasks_common import _groups

if TYPE_CHECKING:
    from collections.abc import Callable


def tasks(
    *,
    include_tasks: list[str] | None = None,
    exclude_tasks: list[str] | None = None,
    include_tags: list[str] | None = None,
    exclude_tags: list[str] | None = None,
):
    "Collects and returns the task groups"

    return {"groups": _groups.GROUPS}

    # # Collect the task groups
    # groups = {
    #     "a_security": _security.GROUP,
    #     "b_lint": _lint.GROUP,
    #     "c_test": _test.GROUP,
    #     "d_browse": _browse.GROUP,
    # }
    # # groups = deepcopy(groups)

    # # # Filter by task names and tags
    # # _filter(groups, include_tasks, exclude_tasks, _matches_name)
    # # _filter(groups, include_tags, exclude_tags, _matches_tag)

    # # # Strip the tags (not part of the poe schema)
    # # _strip_tags(groups)
    # return {"groups": groups}


def _matches_name(task_name: str, _, tasks: list[str]) -> bool:
    "True if a task matches a list of tasks"
    return task_name in tasks


def _matches_tag(_, task: dict, tags: list[str]) -> bool:
    "True if a task matches a list of tags"

    for tag in task["tags"]:
        if tag in tags:
            return True
    return False


def _filter(
    groups: dict,
    include: list[str] | None,
    exclude: list[str] | None,
    ismatch: Callable,
):
    "Applies includes/excludes for a given type of filter"

    if include is not None:
        _filter_low(groups, include, ismatch, default_keep=False)
    if exclude is not None:
        _filter_low(groups, exclude, ismatch, default_keep=True)


def _filter_low(
    groups: dict, filters: list[str], ismatch: Callable, default_keep: bool
):
    "Filters tasks"

    # Iterate through task groups
    empty_groups = []
    for group_name, group in groups.items():
        remove_tasks = []

        # Mark tasks that match the filter
        for task_name, task in group["tasks"].items():
            keep = default_keep
            if ismatch(task_name, task, filters):
                keep = not keep

            # Remove tasks as needed
            if not keep:
                remove_tasks.append(task_name)
        _delete(remove_tasks, group["tasks"])

        # Remove groups that have no tasks remaining
        if len(group) == 0:
            empty_groups.append(group_name)
    _delete(empty_groups, groups)


def _delete(keys: list[str], adict: dict):
    "Removes multiple keys from a dict"
    for key in keys:
        del adict[key]


def _strip_tags(groups: dict):
    "Removes tags from filtered tasks"

    for group in groups.values():
        for task in group["tasks"].values():
            del task["tags"]
