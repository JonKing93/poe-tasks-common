"""
Helper functions to format parts of a poe schema
----------
Functions:
    task        - Formats a task configuration
    utilities   - Formats a collection of private utility tasks
    group       - Formats a task group
    _replace_underscores    - Replaces underscores with hyphens in task names
"""


def task(help: str, **task_config) -> dict:
    "Formats a task configuration"
    return {"help": help} | task_config


def utilities(**tasks: dict) -> dict:
    "Formats the schema for a collection of utility tasks"
    tasks = _replace_underscores(tasks)
    return {f"_{key}": task for key, task in tasks.items()}


def group(heading: str, **tasks: dict) -> dict:
    "Formats the schema for a task group"
    return {"heading": heading, "tasks": _replace_underscores(tasks)}


def _replace_underscores(tasks: dict) -> dict:
    "Replaces underscores with hyphens in task names"
    return {key.replace("_", "-"): task for key, task in tasks.items()}
