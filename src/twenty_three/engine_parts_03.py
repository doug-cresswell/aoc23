import logging
import re
from collections import namedtuple
from pprint import pprint
from typing import List

logger = logging.getLogger(__name__)


# Create named tuple Class for matches
# group is the regex matched string
# line is the line number index
# start and stop are the character index of the match group on the line
Match = namedtuple("Match", "group line start end")

# Named tuple class for characters surrounding the match
Characters = namedtuple("Characters", "above before after below")


def regex_find_numbers(input_text: str) -> Match:
    """
    Find numbers and their positions within the text.

    Return: (List of tuples of ints)
        - number matched
        - line number
        - start index on line
        - stop index on line
    """
    lines = [s.strip() for s in input_text.splitlines()]
    pattern = re.compile(r"[\d]+")

    matches = []
    for i, line in enumerate(lines):
        for m in pattern.finditer(line):
            start, end = m.start(), m.end()
            match = Match(group=m.group(), line=i, start=start, end=end)
            matches.append(match)

    return matches


def get_surrounding(match: Match, input_text: str) -> Characters:
    """
    Get characters surrounding the match position.

    Return:
        - Line Above
        - Precedent Character
        - Antecedent Character
        - Line Below
    """

    lines = [s.strip() for s in input_text.splitlines()]

    # Get single character before and after match
    line = lines[match.line]
    left_start, right_end = max(0, match.start - 1), min(match.end + 1, len(line))
    before = line[left_start : match.start]
    after = line[match.end : right_end]

    # Get characters above and below (including one character either side)
    if match.line > 0:
        above_line = lines[match.line - 1]
        above = above_line[left_start:right_end]
    else:
        above = ""
    if match.line + 1 < len(lines):
        below_line = lines[match.line + 1]
        below = below_line[left_start:right_end]
    else:
        below = ""

    return Characters(above, before, after, below)


def parse_part_numbers(text_input: str) -> List[int]:
    """
    Extract engine part numbers from input text.

    Any number adjacent to a symbol, even diagonally, is a "part number"
    Periods (.) do not count as a symbol.
    """

    # We need:
    # match line number (to get all characters)
    # match (to remove from list of characters)
    # match start and end position in the line (to filter line characters)

    # Findall digit matches
    matches = regex_find_numbers(text_input)
    part_numbers = []
    for match in matches:
        # Get characters surrounding matched number
        characters = get_surrounding(match, text_input)

        # Search for any characters  a symbol other than '.'
        symbol_pattern = re.compile(r"[^\d\.]")
        if symbol_pattern.search("".join(characters)):
            part_numbers.append(int(match.group))

    return part_numbers


def part_one(text_lines: str):
    """Parse the part numbers from the input text and sum the result."""
    numbers = parse_part_numbers(text_lines)
    return sum(numbers)


def part_two(text_lines: str):
    """Parse all the gears and their ratios from their input_text and sum the result."""
    # TODO: Implement gear ratio parse
    ratios = []
    return sum(ratios)


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
