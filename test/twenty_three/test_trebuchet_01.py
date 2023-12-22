import logging
from textwrap import dedent

import pytest

from src.twenty_three.trebuchet_01 import parse, parse_two, solution_one, solution_two


@pytest.fixture
def txt():
    s = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
    return dedent(s)


@pytest.fixture
def answer():
    return 142


@pytest.fixture
def txt_two():
    s = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""
    return dedent(s)


@pytest.fixture
def answer_two():
    return 281


@pytest.mark.parametrize(
    "txt,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_parse(txt, expected):
    logging.debug(f"{txt=}")
    logging.debug(f"{expected=}")
    actual = parse(txt)
    assert actual == expected


@pytest.mark.parametrize(
    "txt,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_parse_two(txt, expected):
    logging.debug(f"{txt=}")
    logging.debug(f"{expected=}")
    actual = parse_two(txt)
    assert actual == expected


def test_solution(txt, txt_two, answer, answer_two):
    actual = solution_one(txt)
    assert actual == answer

    actual = solution_two(txt_two)
    assert actual == answer_two
