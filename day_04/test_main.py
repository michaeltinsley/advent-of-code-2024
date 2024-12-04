from pathlib import Path

from day_04.main import solve_x_mas_word_search, solve_xmas_word_search


def test_part_01():
    path = Path("day_04/test_data.txt")
    expected_result = 18
    result = solve_xmas_word_search(path)
    assert result == expected_result, f"Expected {expected_result} but got {result}"


def test_part_02():
    path = Path("day_04/test_data.txt")
    expected_result = 9
    result = solve_x_mas_word_search(path)
    assert result == expected_result, f"Expected {expected_result} but got {result}"
