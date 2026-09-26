"Defines tasks in the security testing group"

from poe_tasks_common._utils import group

audit = {
    "help": "Check package dependencies for security issues",
    "cmd": "pip-audit",
}

GROUP = group(
    "Security:",
    {
        "audit": audit,
    },
)
