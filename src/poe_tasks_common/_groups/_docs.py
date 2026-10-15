"Task group for documentation"

from poe_tasks_common._format import group, task

output_folder = {
    "help": "Folder containing the built documentation",
    "name": "_output_folder",
    "options": ["-o", "--output"],
    "default": "${DOCS_OUTPUT:-public}",
}


docs = task(
    "Rebuilds the documentation",
    sequence=[
        {"ref": "_rmtree ${_output_folder}"},
        {"cmd": "sphinx-build -qa docs ${_output_folder}"},
    ],
    args=[output_folder],
)

open_docs = task(
    "Opens the built documentation in a web browser",
    ref="_browse-index ${_output_folder}",
    args=[output_folder],
)

GROUP = group(
    "Documentation:",
    docs=docs,
    open_docs=open_docs,
)
