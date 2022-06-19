import pytest

from solutions import (
    GroupAnagrams,
)


@pytest.fixture
def solution():
    return GroupAnagrams()


def test_group_anagrams_case1(solution):
    ref = [[""]]
    strs = [""]
    result = solution.group_anagrams(strs)
    assert all([a == b for a, b in zip(result, ref)])


def test_group_anagrams_case2(solution):
    ref = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.group_anagrams(strs)
    assert all([all([a, b]) for a, b in zip(result, ref)])


def test_group_anagrams_case3(solution):
    ref = [["a"]]
    strs = ["a"]
    result = solution.group_anagrams(strs)
    assert all([a == b for a, b in zip(result, ref)])


def test_constraints(solution):
    with pytest.raises(AssertionError):
        strs = ["f" * 101]
        solution.group_anagrams(strs)

    with pytest.raises(AssertionError):
        strs = ["f"] * (10**4 + 1)
        solution.group_anagrams(strs)

    with pytest.raises(AssertionError):
        strs = ["aBc"]
        solution.group_anagrams(strs)
