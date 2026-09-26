"Defines tasks in the linting group"

from poe_tasks_common._utils import group

format = {
    "help": "Formats the code and its tests",
    "default_item_type": "cmd",
    "sequence": [
        "ruff format ${POE_ROOT}/src ${POE_ROOT}/tests",
        "ruff check ${POE_ROOT}/src ${POE_ROOT}/tests --select I --fix",
    ],
}

lint = {
    "help": "Lints the code and its tests",
    "cmd": "ruff check ${POE_ROOT}/src ${POE_ROOT}/tests",
}

GROUP = group(
    "Linting:",
    {
        "format": format,
        "lint": lint,
    },
)
