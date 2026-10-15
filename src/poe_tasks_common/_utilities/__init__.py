"""
Modules that build private utility tasks
----------
Each of these modules defines utility tasks related to a particular theme. The complete
task collection for each module is stored in its "TASKS" attribute. Then this subpackage
collects all these tasks in its "TASKS" attribute.
----------
Attributes:
    TASKS   - The complete collection of utility tasks

Modules:
    _browse - Utility tasks for opening assets in a web browser
    _delete - Utility tasks for deleting files
"""

from poe_tasks_common._utilities import _browse, _delete

TASKS = _browse.TASKS | _delete.TASKS
