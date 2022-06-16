import pytest

from solutions import (
    IntegerToRomanSolution,
)


@pytest.fixture
def solution():
    return IntegerToRomanSolution()


def test_case_one(solution):
    num = 3
    result = solution.int_to_roman(num)
    assert result == "III"


def test_case_two(solution):
    num = 58
    result = solution.int_to_roman(num)
    assert result == "LVIII"


def test_case_three(solution):
    num = 1994
    result = solution.int_to_roman(num)
    assert result == "MCMXCIV"


def test_constraints(solution):
    with pytest.raises(AssertionError):
        num = 4000
        solution.int_to_roman(num)
