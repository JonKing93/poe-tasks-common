"Task group for testing"

from poe_tasks_common._format import group, task

coverage = task(
    "Prints the coverage report for the tests",
    cmd="coverage report",
)

tests = task(
    "Runs the tests and requires a minimum coverage",
    sequence=[
        {
            "cmd": (
                "pytest tests "
                "--cov=src --cov=tests "
                "--cov-fail-under=${_min_coverage} "
                "--cov-report xml:coverage.xml"
            )
        },
        {"ref": "coverage"},
    ],
    args=[
        {
            "name": "_min_coverage",
            "help": "Minimum required test coverage percent",
            "options": ["--min-coverage"],
            "type": "string",
            "default": "${MIN_COVERAGE:-100}",
        }
    ],
)

htmlcov = task(
    "Builds an HTML coverage report and opens in a web browser",
    sequence=[
        {"ref": "_rmtree htmlcov"},
        {"cmd": "coverage html --skip-covered"},
        {"ref": "_browse-index htmlcov"},
    ],
)


GROUP = group(
    "Testing:",
    tests=tests,
    htmlcov=htmlcov,
    coverage=coverage,
)
