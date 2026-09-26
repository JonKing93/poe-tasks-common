"Utility group for deleting files"

from poe_tasks_common._utils import group

rmtree = {
    "help": "Deletes a project subfolder and its contents",
    "expr": (
        "shutil.rmtree(folder) "
        "if (pathlib.Path(${POE_ROOT}) / folder).exists() "
        "else None"
    ),
    "imports": ["shutil", "pathlib"],
    "args": [
        {
            "name": "folder",
            "help": "A folder path relative to the project root",
            "positional": True,
            "required": True,
        }
    ]
}

delete = {
    "help": "Deletes a project file",
    "expr": (
        "(pathlib.Path(${POE_ROOT}) / file).unlink() "
        "if (pathlib.Path(${POE_ROOT}) / file).exists() "
        "else None"
    ),
    "imports": ["pathlib"],
    "args": [
        {
            "name": "path",
            "help": "A file path relative to the project root",
            "positional": True,
            "required": True,
        }
    ]
}

GROUP = group(
    "Utilities: Delete",
    {
        "delete": delete,
        "rmtree": rmtree,
    }
)
