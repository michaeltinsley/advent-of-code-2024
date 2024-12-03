# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
import re
from dataclasses import dataclass
from enum import Enum
from operator import mul
from pathlib import Path


def load_data(path: Path) -> str:
    """
    Load data from a file.
    """
    with open(path) as file:
        return file.read()


def get_valid_instructions(data: str) -> list[str]:
    """
    Get a list of valid instructions.
    """
    # matches = re.findall(r"mul\(\d+,\d+\)", data)
    matches = re.findall(r"mul\(\d+(?:,\d+)*\)", data)
    return matches


class Operation(Enum):
    MUL = mul


@dataclass
class Instruction:
    op: Operation
    values: list[int | float]


def extract_instruction(instructions: list[str]) -> list[Instruction]:
    """
    Extract instruction from string.
    """
    parsed_instructions = []
    for instruction in instructions:
        match instruction[:3]:
            case "mul":
                values = instruction[4:-1].split(",")
                parsed_instructions.append(
                    Instruction(Operation.MUL, [int(value) for value in values])
                )
            case _:
                raise ValueError("Invalid operation")
    return parsed_instructions


def calculate_instruction_result(path: Path) -> None:
    """
    Calculate the result of the corrected instruction.
    """
    data = load_data(path)
    valid_instructions = get_valid_instructions(data)
    parsed_instructions = extract_instruction(valid_instructions)

    total = 0
    for instruction in parsed_instructions:
        total += instruction.op.value(
            *instruction.values
        )  # This doesn't like len(instruction.values) != 2

    print(f"Data file: {path} Total: {total}")


if __name__ == "__main__":
    path = Path("test_data.txt")
    calculate_instruction_result(path)
    path = Path("data.txt")
    calculate_instruction_result(path)
