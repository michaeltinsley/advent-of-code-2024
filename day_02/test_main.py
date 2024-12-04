from pathlib import Path

from day_02.main import check_data_file


def test_part_01():
    path = Path("day_02/test_data.txt")
    expected_result = 2
    result = check_data_file(path)
    assert result == expected_result, f"Expected {expected_result} but got {result}"


def test_part_02():
    path = Path("day_02/test_data.txt")
    expected_result = 4
    result = check_data_file(path, enable_problem_dampener=True)
    assert result == expected_result, f"Expected {expected_result} but got {result}"
