"Defines tasks in the testing group"

from poe_tasks_common._utils import group

coverage = {
    "help": "Prints the coverage report for the tests",
    "cmd": "coverage report",
}

tests = {
    "help": "Runs the tests and requires a certain coverage",
    "sequence": [
        {
            "cmd": (
                "pytest ${POE_ROOT}/tests "
                "--cov=${POE_ROOT}/src --cov=${POE_ROOT}/tests "
                "--cov-fail-under=${min-coverage} "
                "--cov-report xml:coverage.xml"
            )
        },
        {"ref": "coverage"},
    ],
    "args": [
        {
            "name": "min-coverage",
            "help": "Minimum required test coverage percent",
            "options": ["--cov-fail-under"],
            "type": "string",
            "default": "100",
        }
    ],
}

htmlcov = {
    "help": "Builds an HTML coverage report and opens in a web browser",
    "sequence": [
        {"ref": "rmtree htmlcov"},
        {"cmd": "coverage html --skip-covered"},
        {"ref": "browse-index htmlcov"},
    ]
}


GROUP = group(
    "Testing:",
    {
        "tests": tests,
        "htmlcov": htmlcov,
        "coverage": coverage,
    },
)
