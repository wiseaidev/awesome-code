import pytest

from solutions import (
    IsomorphicStrings,
)


@pytest.fixture
def solution():
    return IsomorphicStrings()


def test_is_isomorphic_case1(solution):
    strs = ["egg", "add"]
    assert solution.is_isomorphic(*strs) is True


def test_is_isomorphic_case2(solution):
    strs = ["foo", "bar"]
    assert solution.is_isomorphic(*strs) is False


def test_is_isomorphic_case3(solution):
    strs = ["paper", "title"]
    assert solution.is_isomorphic(*strs) is True


def test_constraints(solution):
    with pytest.raises(AssertionError):
        strs = ["f" * (5 * 10**4 + 1), ["a"] * (5 * 10**4 + 1)]
        solution.is_isomorphic(*strs)

    with pytest.raises(AssertionError):
        strs = ["f" * (5 * 10**4), ["a"] * (4 * 10**4)]
        solution.is_isomorphic(*strs)
