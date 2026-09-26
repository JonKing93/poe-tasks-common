

from poe_tasks_common._groups import _browse, _delete, _lint, _security, _test


GROUPS = {
    "a_security": _security.GROUP,
    "b_lint": _lint.GROUP,
    "c_test": _test.GROUP,
    "d_browse": _browse.GROUP,
    "e_delete": _delete.GROUP,
}