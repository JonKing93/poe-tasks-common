"Task group for linting and formatting"

from poe_tasks_common._format import group, task

format = task(
    "Formats the code and its tests",
    default_item_type="cmd",
    sequence=[
        "ruff format src tests",
        "ruff check src tests --select I --fix",
    ],
)

lint = task(
    help="Lints the code and its tests",
    cmd="ruff check src tests",
)

GROUP = group(
    "Linting:",
    format=format,
    lint=lint,
)
