"Task group for managing the developer environment"

from poe_tasks_common._format import group, task

sync = task(
    "Syncs the development environment",
    cmd="uv sync --all-groups --all-extras",
)

upgrade = task(
    "Syncs and upgrades the development environment",
    ref="sync --upgrade",
)

GROUP = group(
    "Environment:",
    sync=sync,
    upgrade=upgrade,
)
