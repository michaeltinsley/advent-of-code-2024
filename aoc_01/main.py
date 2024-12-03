# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from collections import Counter
from operator import abs, sub
from pathlib import Path
from typing import Tuple


def load_data(path: Path) -> Tuple[list[int], list[int]]:
    """
    Load AOC data from file.
    """
    with open(path, "r") as file:
        data = file.readlines()

    x, y = zip(*(map(int, row.split()) for row in data))
    return list(x), list(y)


def find_total_distance(x: list[int], y: list[int]) -> int:
    """
    Find the total distance between two lists of integers.

    :param x: The first list of integers.
    :param y: The second list of integers.
    :return: The total distance between the two lists.
    """
    x, y = sorted(x), sorted(y)
    abs_values = list(map(abs, map(sub, x, y)))
    total_value = sum(abs_values)
    return total_value


def find_similarity_score(x: list[int], y: list[int]) -> int:
    """
    Find the similarity score between two lists of integers.

    :param x: The first list of integers.
    :param y: The second list of integers.
    :return: The similarity score between the two lists.
    """
    lookup = Counter(y)
    simlarity_score = sum(x * lookup.get(x, 0) for x in x)
    return simlarity_score


def load_and_find_distance(path: Path) -> int:
    """
    Load AOC data from file and find the total distance between two lists of integers.
    """
    x, y = load_data(path)
    return find_total_distance(x, y)


def load_and_find_similarity_score(path: Path) -> int:
    """
    Load AOC data from file and find the similarity score between two lists of integers.
    """
    x, y = load_data(path)
    return find_similarity_score(x, y)


if __name__ == "__main__":
    path = Path("aoc_01/data.txt")

    distance = load_and_find_distance(path)
    print(f"Part 01: Distance for {path} = {distance}")

    similarity = load_and_find_similarity_score(path)
    print(f"Part 02: Similarity score for {path} = {similarity}")
