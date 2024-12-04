from pathlib import Path


def load_data(path: Path) -> list[str]:
    """
    Load data from a file.
    """
    with open(path) as file:
        data = file.read().splitlines()
    return data


class WordSearchSolver:
    def __init__(self, grid: list[str]) -> None:
        """
        Initialize the word search solver with a grid.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = self._get_search_directions()

    def _get_search_directions(self) -> list[tuple[int, int]]:
        """
        Define all possible search directions.
        """
        return [
            (-1, 0),  # up
            (0, 1),  # right
            (1, 0),  # down
            (0, -1),  # left
            (-1, 1),  # diagonal up-right
            (1, 1),  # diagonal down-right
            (1, -1),  # diagonal down-left
            (-1, -1),  # diagonal up-left
        ]

    def _is_valid_position(self, row: int, col: int) -> bool:
        """
        Check if the given position is within grid boundaries.
        """
        return 0 <= row < self.rows and 0 <= col < self.cols

    def _find_word_from_start(
        self,
        start_row: int,
        start_col: int,
        direction: tuple[int, int],
        target_word: str,
    ) -> bool:
        """
        Check if target word exists starting from a specific position in a given
        direction.
        """
        d_row, d_col = direction

        for i, letter in enumerate(target_word):
            curr_row = start_row + i * d_row
            curr_col = start_col + i * d_col

            # Check if current position is valid and matches the letter
            if (
                not self._is_valid_position(curr_row, curr_col)
                or self.grid[curr_row][curr_col] != letter
            ):
                return False

        return True

    def count_word_occurrences(self, target_word: str) -> int:
        """
        Count all occurrences of a target word in the grid.
        """
        word_count = 0

        # Check every cell as a potential start of the word
        for row in range(self.rows):
            for col in range(self.cols):
                # Try all possible search directions
                for direction in self.directions:
                    if self._find_word_from_start(row, col, direction, target_word):
                        word_count += 1

        return word_count


def solve_xmas_word_search(path: Path) -> int:
    """
    Solve the XMAS word search problem.
    """
    grid = load_data(path)
    solver = WordSearchSolver(grid)
    return solver.count_word_occurrences("XMAS")


if __name__ == "__main__":
    path = Path("day_04/data.txt")
    result = solve_xmas_word_search(path)
    print(f"Part 01: Data file: {path} Total: {result}")