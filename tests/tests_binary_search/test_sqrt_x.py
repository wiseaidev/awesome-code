import pytest

from solutions import (
    MySqrt,
)


@pytest.fixture
def solution():
    return MySqrt()


def test_sqrt_case_1(solution):
    assert 2 == solution.sqrt(4)


def test_sqrt_case_2(solution):
    assert 2 == solution.sqrt(8)
