import pytest

from src.twenty_three.engine_parts_03 import (
    Characters,
    Match,
    get_surrounding,
    parse,
    part_one,
    regex_find_numbers,
)


@pytest.fixture
def example_input():
    def read(path):
        with open(path) as f:
            txt = f.read().strip()
        return txt

    stem = "2023_03"
    return read(f"inputs/{stem}_example.txt")


@pytest.fixture
def example_snippet(example_input):
    """Shorter input for writing less test results."""
    lines = example_input.strip().split("\n")
    return "\n".join(lines[:4])


@pytest.fixture
def example_matches():
    return [
        # "group line start end"
        Match("467", 0, 0, 3),
        Match("114", 0, 5, 8),
        Match("35", 2, 2, 4),
        Match("633", 2, 6, 9),
    ]


@pytest.fixture
def example_characters():
    return [
        # above before after below
        Characters("", "", ".", "...*"),
        Characters("", ".", ".", "....."),
        Characters("..*.", ".", ".", "...."),
        Characters(".....", ".", ".", ".#..."),
    ]


def test_regex_find_numbers(example_snippet, example_matches):
    actual_matches = regex_find_numbers(example_snippet)

    assert len(actual_matches) == len(example_matches)

    for i, actual in enumerate(actual_matches):
        assert isinstance(actual, Match)
        assert actual == example_matches[i]


def test_get_surrounding(example_snippet, example_matches, example_characters):
    assert len(example_matches) == len(example_characters)
    for i, m in enumerate(example_matches):
        actual = get_surrounding(m, example_snippet)
        assert isinstance(actual, Characters)
        assert actual == example_characters[i]


def test_parse(example_input):
    lines = example_input.split("\n")
    assert lines[0] == "467..114.."

    actual = parse(example_input)
    expected = [
        467,
        35,
        633,
        617,
        592,
        755,
        664,
        598,
    ]
    assert actual == expected


def test_part_one(example_input):
    actual = part_one(example_input)
    expected = 4361
    assert actual == expected


# @pytest.mark.xfail("Need output for part two example")
# def test_part_two(example_input):
#     actual = part_two(example_input)
#     expected = None
#     raise NotImplementedError("Test not implemented, add expected for part two")
#     assert actual == expected
