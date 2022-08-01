import pytest

from solutions import (
    IsSubsequence,
)


@pytest.fixture
def solution():
    return IsSubsequence()


def test_is_subsequence_case1(solution):
    strs = ["abc", "ahbgdc"]
    assert solution.is_subsequence(*strs) is True


def test_is_subsequence_case2(solution):
    strs = ["axc", "ahbgdc"]
    assert solution.is_subsequence(*strs) is False


def test_constraints(solution):
    with pytest.raises(AssertionError):
        strs = ["a" * (101), ["a"] * (10**4)]
        solution.is_subsequence(*strs)

    with pytest.raises(AssertionError):
        strs = ["a" * (101), ["a"] * (10**4)]
        solution.is_subsequence(*strs)
