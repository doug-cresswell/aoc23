import pytest

from src.twenty_three.engine_parts_03 import (
    parse,
    part_one,
    part_two,
    regex_find_diagonal,
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


def test_regex_diagonal(example_snippet):
    actual_matches = regex_find_diagonal(example_snippet)

    expected_matches = [
        ("", "", "467", ".", "...*"),
        ("", ".", "114", ".", "....."),
        ("..*.", ".", "35", ".", "...."),
        (".....", ".", "633", ".", ".#..."),
    ]

    assert len(actual_matches) == len(expected_matches)

    for i, actual in enumerate(actual_matches):
        assert actual == expected_matches[i]


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


@pytest.mark.xfail("Need output for part two example")
def test_part_two(example_input):
    actual = part_two(example_input)
    expected = None
    raise NotImplementedError("Test not implemented, add expected for part two")
    assert actual == expected
