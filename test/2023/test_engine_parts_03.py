import pytest

from src.twenty_three.engine_parts_03 import part_one


@pytest.fixture
def example_input():
    def read(path):
        with open(path) as f:
            txt = f.read().strip()
        return txt

    stem = "2023_03"
    return read(f"inputs/{stem}_example.txt")


def test_parse(example_input):
    lines = example_input.split("\n")
    assert lines[0] == "467..114.."
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
    actual = part_one(example_input)
    assert actual == expected


def test_part_one(example_input):
    actual = part_one(example_input)
    expected = 4361
    assert actual == expected


@pytest.mark.xfail("Need output for part two example")
def test_part_two(example_input):
    actual = part_one(example_input)
    expected = None
    raise NotImplementedError("Test not implemented, add expected for part two")
    assert actual == expected
