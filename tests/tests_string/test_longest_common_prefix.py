import pytest

from solutions import (
    LongestCommonPrefix,
)


@pytest.fixture
def solution():
    return LongestCommonPrefix()


def test_longest_common_prefix_case1(solution):
    strs = ["flower", "flow", "flight"]
    # list is passed by reference
    result = solution.longest_common_prefix(strs)
    assert result == "fl"


def test_longest_common_prefix_case2(solution):
    strs = ["flower", "flow", "flight"]
    # list is passed by reference
    result = solution.longest_common_prefix(strs)
    assert result == "fl"


def test_longest_common_prefix_case3(solution):
    strs = []
    # list is passed by reference
    result = solution.longest_common_prefix(strs)
    assert result == ""


def test_constraints(solution):
    with pytest.raises(AssertionError):
        strs = ["f" * 201]
        solution.longest_common_prefix(strs)

    with pytest.raises(AssertionError):
        strs = ["f"] * 201
        solution.longest_common_prefix(strs)

    with pytest.raises(AssertionError):
        strs = ["aBc"]
        solution.longest_common_prefix(strs)
