from pathlib import Path

from aoc_03.main import calculate_instruction_result


def test_part_01():
    path = Path("aoc_03/test_data.txt")
    expected_result = 161
    result = calculate_instruction_result(path)
    assert result == expected_result, f"Expected {expected_result} but got {result}"


def test_part_02():
    path = Path("aoc_03/test_data2.txt")
    expected_result = 48
    result = calculate_instruction_result(path, conditionals_enabled=True)
    assert result == expected_result, f"Expected {expected_result} but got {result}"
