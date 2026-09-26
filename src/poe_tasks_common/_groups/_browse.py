"Utility group for opening files in a web browser"

from poe_tasks_common._utils import group

browse = {
    "help": "Opens a URI (file or web URL) in a web browser",
    "expr": "webbrowser.open(uri)",
    "imports": ["webbrowser"],
    "args": [
        {
            "name": "uri",
            "help": "The target URI (file or web URL) to open",
            "positional": True,
            "required": True,
        }
    ],
}

browse_file = {
    "help": "Opens a project file in a web browser",
    "expr": "webbrowser.open( (pathlib.Path(${POE_ROOT}) / path).as_uri() )",
    "imports": ["webbrowser", "pathlib"],
    "args": [
        {
            "name": "path",
            "help": "A file path relative to the project root",
            "positional": True,
            "required": True,
        }
    ]
}

browse_index = {
    "help": "Opens a project subfolder's index.html file",
    "ref": "browse-file ${folder}/index.html",
    "args": [
        {
            "name": "folder",
            "help": "A folder path relative to the project root",
            "positional": True,
            "required": True,
        }
    ]
}

GROUP = group(
    "Utilities: Browse",
    {
        "browse": browse,
        "browse-file": browse_file,
        "browse-index": browse_index,
    },
)