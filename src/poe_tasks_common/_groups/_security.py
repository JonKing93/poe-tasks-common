"Task group for security testing"

from poe_tasks_common._format import group, task

audit = task(
    "Check package dependencies for security issues",
    cmd="pip-audit",
)

GROUP = group(
    "Security:",
    audit=audit,
)
