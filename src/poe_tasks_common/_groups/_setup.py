"Task group for first time setup"

from poe_tasks_common._format import group, task

install_precommit = task(
    "Installs pre-commit",
    default_item_type="cmd",
    sequence=[
        "uv tool install pre-commit --with pre-commit-uv --force-reinstall",
        "pre-commit install",
    ],
)

setup = task(
    "Syncs all dependencies and installs pre-commit",
    default_item_type="ref",
    sequence=[
        "sync --frozen",
        "install-precommit",
    ],
)

GROUP = group(
    "Setup:",
    setup=setup,
    install_precommit=install_precommit,
)
