"""
Modules that build task groups
----------
Each of these modules defines a particular task group, which is stored in its "GROUP"
attribute. Then this subpackage collects all the task groups in its "GROUPS" attribute.
----------
Attributes:
    GROUP       - The complete collection of task groups

Modules:
    _docs       - Documentation task group
    _env        - Development environment task group
    _lint       - Formatting and linting task group
    _security   - Security testing task group
    _setup      - First time setup task group
    _test       - Testing task group
"""

from poe_tasks_common._groups import _docs, _env, _lint, _security, _setup, _test

GROUPS = {
    "100_setup": _setup.GROUP,
    "200_env": _env.GROUP,
    "300_security": _security.GROUP,
    "400_lint": _lint.GROUP,
    "500_test": _test.GROUP,
    "600_docs": _docs.GROUP,
}
