from pathlib import Path

from .main import load_and_find_distance, load_and_find_similarity_score


def test_part_01():
    path = Path("aoc_01/test_data.txt")
    expected_result = 11
    result = load_and_find_distance(path)
    assert result == expected_result, f"Expected {expected_result} but got {result}"


def test_part_02():
    path = Path("aoc_01/test_data.txt")
    expected_result = 31
    result = load_and_find_similarity_score(path)
    assert result == expected_result, f"Expected {expected_result} but got {result}"
