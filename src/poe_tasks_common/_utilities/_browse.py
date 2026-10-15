"Utility group for opening files in a web browser"

from poe_tasks_common._format import task, utilities

browse = task(
    "Opens a URI (file or web URL) in a web browser",
    expr="webbrowser.open(_uri)",
    imports=["webbrowser"],
    args=[
        {
            "name": "_uri",
            "help": "The target URI (file or web URL) to open",
            "positional": True,
            "required": True,
        }
    ],
)

browse_file = task(
    "Opens a project file in a web browser",
    expr="webbrowser.open( pathlib.Path(_path).as_uri() )",
    imports=["webbrowser", "pathlib"],
    args=[
        {
            "name": "_path",
            "help": "A file path relative to the project root",
            "positional": True,
            "required": True,
        }
    ],
)

browse_index = task(
    "Opens a project subfolder's index.html file",
    ref="_browse-file ${_folder}/index.html",
    args=[
        {
            "name": "_folder",
            "help": "A folder path relative to the project root",
            "positional": True,
            "required": True,
        }
    ],
)

TASKS = utilities(
    browse=browse,
    browse_file=browse_file,
    browse_index=browse_index,
)
