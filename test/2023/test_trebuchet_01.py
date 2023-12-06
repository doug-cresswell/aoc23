from textwrap import dedent

import pytest

from src.app.trebuchet_01 import parse, solution


@pytest.fixture
def input():
    s = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
    return dedent(s)


@pytest.fixture
def answer():
    return 142


@pytest.mark.parametrize(
    "input,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_parse(input, expected):
    print(input, expected)
    actual = parse(input)
    assert actual == expected


def test_solution(input, answer):
    actual = solution(input)
    assert actual == answer
    assert actual == answer
    assert actual == answer
    assert actual == answer
