import pytest

from src.twenty_three.engine_parts_03 import (
    Characters,
    Match,
    get_surrounding,
    parse_gear_parts,
    parse_part_numbers,
    part_one,
    part_two,
    regex_find_gears,
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
def example_input_short(example_input):
    """Shorter input for writing less test results."""
    lines = example_input.strip().split("\n")
    return "\n".join(lines[:4])


@pytest.fixture
def parts_matches():
    return [
        # "group line start end"
        Match("467", 0, 0, 3),
        Match("114", 0, 5, 8),
        Match("35", 2, 2, 4),
        Match("633", 2, 6, 9),
        Match("617", 4, 0, 3),
        Match("58", 5, 7, 9),
        Match("592", 6, 2, 5),
        Match("755", 7, 6, 9),
        Match("664", 9, 1, 4),
        Match("598", 9, 5, 8),
    ]


@pytest.fixture
def gears_matches():
    return [
        # "group line start end"
        Match(group="*", line=1, start=3, end=4),
        Match(group="*", line=4, start=3, end=4),
        Match(group="*", line=8, start=5, end=6),
    ]


@pytest.fixture
def parts_matches_short(parts_matches):
    return parts_matches[:4]


@pytest.fixture
def characters_short():
    return [
        # above before after below
        Characters("", "", ".", "...*"),
        Characters("", ".", ".", "....."),
        Characters("..*.", ".", ".", "...."),
        Characters(".....", ".", ".", ".#..."),
    ]


def test_regex_find_numbers(example_input, parts_matches):
    actual_matches = regex_find_numbers(example_input)

    assert len(actual_matches) == len(parts_matches)

    for i, actual in enumerate(actual_matches):
        assert isinstance(actual, Match)
        assert actual == parts_matches[i]


def test_get_surrounding(example_input_short, parts_matches_short, characters_short):
    assert len(parts_matches_short) == len(characters_short)
    for i, m in enumerate(parts_matches_short):
        actual = get_surrounding(m, example_input_short)
        assert isinstance(actual, Characters)
        assert actual == characters_short[i]


def test_parse_part_numbers(parts_matches, example_input):
    lines = example_input.split("\n")
    assert lines[0] == "467..114.."

    actual = parse_part_numbers(matches=parts_matches, text_input=example_input)
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


def test_regex_find_gears(example_input, gears_matches):
    actual = regex_find_gears(example_input)
    assert actual == gears_matches


def test_parse_gear_parts(gears_matches, parts_matches, example_input):
    expected_parts = [(467, 35), (755, 598)]
    actual_parts = parse_gear_parts(
        gear_matches=gears_matches, part_matches=parts_matches, input_text=example_input
    )
    for i, actual in enumerate(actual_parts):
        assert actual == expected_parts[i]


def test_part_one(example_input):
    actual = part_one(example_input)
    expected = 4361
    assert actual == expected


def test_part_two(example_input):
    actual = part_two(example_input)
    expected = 467835
    assert actual == expected
