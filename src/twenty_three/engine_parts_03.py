import logging
from pprint import pprint

logger = logging.getLogger(__name__)


def parse(text: str):
    """
    Extract engine part numbers from input text.

    Any number adjacent to a symbol, even diagonally, is a "part number"
    Periods (.) do not count as a symbol.
    """

    pass


def part_one(text_lines: str):
    # Your solution for part one
    pass


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
