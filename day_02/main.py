from pathlib import Path


def load_data(path: Path) -> list[list[int]]:
    """
    Load data from a file.
    """
    with open(path) as file:
        data = [list(map(int, row.split())) for row in file]
    return data


def is_monotonic(report: list[int]) -> bool:
    """
    Check if the report is monotonic, either increasing or decreasing.
    """
    return report == sorted(report) or report == sorted(report, reverse=True)


def has_valid_deltas(report: list[int]) -> bool:
    """
    Check if the reports deltas are within the allowed range.
    """
    deltas = [j - i for i, j in zip(report[:-1], report[1:])]
    return all(1 <= abs(delta) <= 3 for delta in deltas)


def is_safe_report(report: list[int]) -> bool:
    """
    Assert the two checks to ensure a report is safe.
    """
    return is_monotonic(report) and has_valid_deltas(report)


def problem_dampener(report: list[int]) -> bool:
    """
    Enable the problem dampener.
    """
    for i in range(len(report)):
        # Loop through and check each subreport is safe.
        if is_safe_report(report[:i] + report[i + 1 :]):
            return True
    return False


def check_data_file(path: Path, enable_problem_dampener: bool = False) -> int:
    """
    Check the data from a file.
    """
    data = load_data(path)

    if enable_problem_dampener:
        safety_check = [
            is_safe_report(report) or problem_dampener(report) for report in data
        ]
    else:
        safety_check = [is_safe_report(report) for report in data]

    return sum(safety_check)


if __name__ == "__main__":
    path = Path("day_02/data.txt")

    number_safe = check_data_file(path)
    print(f"Part 01: Data: {path} Number of Safe Reports: {number_safe}")

    number_safe = check_data_file(path, enable_problem_dampener=True)
    print(f"Part 02: Data: {path} Number of Safe Reports: {number_safe}")
