import logging
import re
from pprint import pprint
from typing import List, Tuple

logger = logging.getLogger(__name__)


def regex_find_diagonal(input_text: str) -> List[Tuple[str]]:
    """Find potential part numbers with their surrounding characters."""
    pattern = re.compile(r"[\d]+")

    lines = [s.strip() for s in input_text.splitlines()]

    matches = []
    for i, line in enumerate(lines):
        logger.debug(f"{i=}\t{line=}")
        for m in pattern.finditer(line):
            logger.debug(m.group())
            start, end = m.start(), m.end()
            left_start, right_end = max(0, start - 1), min(end + 1, len(line))

            above = "" if i == 0 else lines[i - 1][left_start:right_end]
            left = line[left_start:start]
            right = line[end:right_end]
            below = lines[i + 1][left_start:right_end] if i + 1 < len(lines) else ""

            match = (above, left, m.group(), right, below)
            matches.append(match)
        logger.debug()

    return matches


def parse(text_input: str) -> List[int]:
    """
    Extract engine part numbers from input text.

    Any number adjacent to a symbol, even diagonally, is a "part number"
    Periods (.) do not count as a symbol.
    """

    # Findall digit matches
    matches = regex_find_diagonal(text_input)
    part_numbers = []
    for match in matches:
        # Get numbers and characters immediately to sides
        match = list(match)
        number = match.pop(2)

        # Any characters surrounding match group are a symbol other than '.'
        surrounding = "".join(match)
        if any(s != "." for s in surrounding):
            part_numbers.append(int(number))

    return part_numbers


def part_one(text_lines: str):
    """Parse the part numbers from the input text and sum the result."""
    numbers = parse(text_lines)
    return sum(numbers)


def part_two(text_lines: str):
    # Your solution for part two
    pass


def main():
    def read(path):
        with open(path) as f:
            txt = f.read().strip()
        return txt

    # Update to challenge number
    stem = "2023_03"

    input_text = dict(
        example=read(f"inputs/{stem}_example.txt"),
        actual=read(f"inputs/{stem}.txt"),
    )

    answers = {
        "part_one": {k: part_one(v) for k, v in input_text.items()},
        "part_two": {k: part_two(v) for k, v in input_text.items()},
    }

    pprint(answers)


if __name__ == "__main__":
    main()
