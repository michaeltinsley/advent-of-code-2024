# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
import logging
from pathlib import Path
from venv import logger

logger = logging.getLogger(__name__)


def load_data(path: Path) -> list[list[int]]:
    """
    Load data from a file.
    """
    with open(path) as file:
        data = [list(map(int, row.split())) for row in file]
    return data


def check_report_monotonicity(report: list[int]) -> bool:
    """
    Check if the report is monotonic.
    """
    return report == sorted(report) or report == sorted(report, reverse=True)


def check_report_deltas(report: list[int]) -> bool:
    """
    Check if the reports deltas are consistent.
    """
    deltas = [j - i for i, j in zip(report[:-1], report[1:])]
    return all(1 <= abs(delta) <= 3 for delta in deltas)


def check_report_safe(report: list[int]) -> bool:
    """
    Check if the report is safe.
    """
    monotonic = check_report_monotonicity(report)
    deltas = check_report_deltas(report)
    logger.info(f"Report: {report} Monotonic: {monotonic}, Deltas: {deltas}")
    return monotonic and deltas


def check_data_file(path: Path) -> None:
    """
    Check the data from a file.
    """
    data = load_data(path)
    safety_check = [check_report_safe(report) for report in data]
    print(f"Data: {path} Number of Safe Reports: {sum(safety_check)}")


if __name__ == "__main__":
    check_data_file("test_data.txt")
    check_data_file("data.txt")
