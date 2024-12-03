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
    Get a list of valid instructions. We only care about mul, do, and don't.
    """
    return re.findall(r"mul\(\d+,\d+\)|don't|do", data)


class Operation(Enum):
    """
    Operation enum - I assumed part 02 would require more operations .
    """

    MUL = mul
    DO = True
    DONT = False


@dataclass
class Instruction:
    """
    Instruction dataclass.
    Again, I assumed part 02 would require more operations so this made sense XD.
    """

    op: Operation
    x: int | None = None
    y: int | None = None


def extract_instruction(instructions: list[str]) -> list[Instruction]:
    """
    Extract instruction from string.

    :param instructions: List of raw instruction strings.
    :return: List of Instruction objects.
    """
    parsed_instructions = []
    for instruction in instructions:
        match instruction.split("(")[0]:
            case "mul":
                values = instruction[4:-1].split(",")
                parsed_instructions.append(
                    Instruction(
                        op=Operation.MUL,
                        x=int(values[0]),
                        y=int(values[1]),
                    )
                )
            case "do":
                parsed_instructions.append(Instruction(op=Operation.DO))
            case "don't":
                parsed_instructions.append(Instruction(op=Operation.DONT))
            case _:
                raise ValueError("Invalid operation")
    return parsed_instructions


def calculate_instruction_result(
    path: Path,
    conditionals_enabled: bool = False,
) -> None:
    """
    Calculate the result of the corrected instruction.

    :param path: Path to the data file.
    :param conditionals_enabled: Enable conditionals for part 02.
    """
    data = load_data(path)
    valid_instructions = get_valid_instructions(data)
    parsed_instructions = extract_instruction(valid_instructions)

    if not conditionals_enabled:  # Remove conditionals for part 01
        parsed_instructions = [
            instruction
            for instruction in parsed_instructions
            if instruction.op == Operation.MUL
        ]
    total = 0
    state = True  # Set default state to True
    for instruction in parsed_instructions:
        match instruction.op:
            case Operation.MUL:
                if (
                    state
                ):  # Only calculate if state is True. For part 01, state is always True
                    total += instruction.op.value(
                        instruction.x,
                        instruction.y,
                    )
            case Operation.DO:
                state = True
            case Operation.DONT:
                state = False

    print(
        f"Data file: {path} Total: {total} Conditionals enabled: {conditionals_enabled}"
    )


if __name__ == "__main__":
    # Part 01
    calculate_instruction_result(Path("test_data.txt"))
    calculate_instruction_result(Path("data.txt"))

    # Part 02
    calculate_instruction_result(Path("test_data2.txt"), conditionals_enabled=True)
    calculate_instruction_result(Path("data.txt"), conditionals_enabled=True)
