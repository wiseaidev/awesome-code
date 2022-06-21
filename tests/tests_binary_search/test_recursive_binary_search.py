import pytest

from solutions import (
    RecursiveBinarySearch,
)


@pytest.fixture
def solution():
    return RecursiveBinarySearch()


def test_binary_search(solution):
    nums = [-1, 0, 3, 5, 9, 12]
    result = solution.search(nums, 9)
    assert result == 4
    nums = [-1, 0, 3, 5, 9, 12]
    result = solution.search(nums, 2)
    assert result == -1


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = [1] * (10**4 + 1)
        solution.search(nums, 10)

    with pytest.raises(AssertionError):
        nums = [10**4]
        solution.search(nums, 10)

    with pytest.raises(AssertionError):
        nums = [4, 3, 1, 1, 1]
        solution.search(nums, 1)

    with pytest.raises(AssertionError):
        nums = [4, 3, 2, 1]
        solution.search(nums, 1)

    with pytest.raises(AssertionError):
        nums = [1, 2, 3, 4]
        solution.search(nums, 10**4)
