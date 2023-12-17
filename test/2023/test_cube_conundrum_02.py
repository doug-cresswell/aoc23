from textwrap import dedent

import pytest

from src.twenty_three.cube_conundrum_02 import CubeSet, parse


@pytest.fixture
def example_text():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    return dedent(s)


@pytest.fixture
def example_games():
    return [
        [  # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            CubeSet(blue=3, red=4),
            CubeSet(blue=6, green=2, red=1),
            CubeSet(green=2),
        ],
        [  # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            CubeSet(
                blue=1,
                green=2,
            ),
            CubeSet(blue=4, green=3, red=1),
            CubeSet(
                blue=1,
                green=1,
            ),
        ],
        [  # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            CubeSet(blue=6, green=8, red=20),
            CubeSet(blue=5, green=13, red=4),
            CubeSet(green=5, red=1),
        ],
        [  # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            CubeSet(blue=6, green=1, red=3),
            CubeSet(green=3, red=6),
            CubeSet(blue=15, green=3, red=14),
        ],
        [  # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            CubeSet(blue=1, green=3, red=6),
            CubeSet(blue=2, green=2, red=1),
        ],
    ]


def test_parse(example_text, example_games):
    lines = example_text.strip().split("\n")
    for i, line in enumerate(lines):
        cubesets = parse(line)
        for j, actual in enumerate(cubesets):
            expected = example_games[i][j]
            assert actual == expected, f"{line=}\n{i=}\n{j=}\n{actual=}\n{expected=}"


class TestCubeSet:
    def test_possible(self):
        a = CubeSet("aabc")
        b = CubeSet("abc")
        assert a.possible(b)
        assert a == CubeSet("aabc")

        a = CubeSet("aabc")
        assert a.possible(a)

        a = CubeSet("aabc")
        b = CubeSet("abcd")
        assert not a.possible(b)

    def test_power(self):
        cubesets = [
            CubeSet(red=4, green=2, blue=6),
            CubeSet(red=1, green=3, blue=4),
            CubeSet(red=20, green=13, blue=6),
            CubeSet(red=14, green=3, blue=15),
            CubeSet(red=6, green=3, blue=2),
        ]
        powers = [48, 12, 1560, 630, 36]
        assert len(cubesets) == len(powers)
        for i, cubes in enumerate(cubesets):
            actual = cubes.power()
            assert actual == powers[i]
