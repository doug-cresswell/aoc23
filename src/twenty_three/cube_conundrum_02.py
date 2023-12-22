from __future__ import annotations

import ast
from collections import Counter
from functools import reduce
from pprint import pprint
from typing import List
from ..logger_config import get_logger


logger = get_logger(__name__)


class CubeSet(Counter):
    """Counter Class for set of coloured cubes."""

    def __ior__(self, other: CubeSet) -> CubeSet:
        return CubeSet(super().__ior__(other))

    def __or__(self, other: CubeSet) -> CubeSet:
        return CubeSet(super().__or__(other))

    def possible(self, other: CubeSet) -> bool:
        """Determine if other CubeSet can be created from self."""
        copy = self.copy()
        copy.subtract(other)
        return all(v >= 0 for v in copy.values())

    def power(self) -> int:
        """
        Multiply the numbers of cubes together to find the 'power'.

        The power of a CubeSet is equal to the numbers of red, green, and blue cubes
        multiplied together.

        I feel that this should be called the product, not the power... but oh well...
        I'm not the author of the tasks.

        Example:
        >>> c = Cubeset(red=4, green=2, blue=6)
        >>> c.power()
        48
        """
        product = 1
        # TODO: functools.reduce
        for v in self.values():
            product *= v
        return product


def parse(text: str) -> List[CubeSet]:
    """
    Parse useful input from text representation of a game.

    Example:
    >>> game = "Game 1: 3 blue, 4 red; 1 red, 2 green; 2 green"
    >>> output = parse(game)
    >>> print(output)
    [{'blue': '3', 'red': '4'}, {'red': '1', 'green': '2'}, {'green': '2'}]
    """

    # Remove game reference number
    start = text.index(":") + 1
    text = text[start:]
    # "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    # Split into array of results
    games = []
    for game in text.split(";"):
        game = game.strip()
        # "3 blue, 4 red"

        # Split into array of cubes and reverse string order
        cubes = [(s.strip().split(" ")) for s in game.split(",")]
        cubes = [t[::-1] for t in cubes]

        # Build repr
        cubes = ["'{}': {}".format(*t) for t in cubes]
        cube_repr = "{" + ", ".join(cubes) + "}"

        # Eval as Cubeset
        games.append(CubeSet(ast.literal_eval(cube_repr)))

    return games


def part_one(text_lines: str) -> int:
    """
    Possible Games.

    Determine which games would have been possible if the bag had been loaded with only
    12 red cubes, 13 green cubes, and 14 blue cubes.
    What is the sum of the IDs of those games?
    """

    # The inventory of cubes
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    inventory = CubeSet(red=12, green=13, blue=14)

    # Get list of games possible given inventory
    possible_games = []
    for i, game in enumerate(text_lines.split("\n")):
        draws = parse(game)
        if all([inventory.possible(d) for d in draws]):
            possible_games.append(i + 1)

    # Sum game numbers
    return sum(possible_games)


def part_two(text_lines: str) -> CubeSet:
    """
    The power of the minimum cubesets.

    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?
    """
    powers = []
    for game in text_lines.split("\n"):
        # Find the minimum cubeset
        draws = parse(game)
        minimum_set = reduce(lambda x, y: x | y, draws)

        if not isinstance(minimum_set, CubeSet):
            msg = f"Expected CubeSet, got {type(minimum_set)}"
            raise TypeError(msg)

        # Find the 'power' of the minimum set
        powers.append(minimum_set.power())

    # Sum the powers
    return sum(powers)


def main():
    def read(path):
        with open(path) as f:
            txt = f.read().strip()
        return txt

    stem = "2023_02"

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
