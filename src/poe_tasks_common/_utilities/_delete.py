"Utility group for deleting files"

from poe_tasks_common._format import task, utilities

rmtree = task(
    "Deletes a project subfolder and its contents",
    expr="shutil.rmtree(_folder) if pathlib.Path(_folder).exists() else None",
    imports=["shutil", "pathlib"],
    args=[
        {
            "name": "_folder",
            "help": "A folder path relative to the project root",
            "positional": True,
            "required": True,
        }
    ],
)

delete = task(
    "Deletes a project file",
    expr="pathlib.Path(_file).unlink() if pathlib.Path(_file).exists() else None",
    imports=["pathlib"],
    args=[
        {
            "name": "_file",
            "help": "A file path relative to the project root",
            "positional": True,
            "required": True,
        }
    ],
)

TASKS = utilities(
    delete=delete,
    rmtree=rmtree,
)
