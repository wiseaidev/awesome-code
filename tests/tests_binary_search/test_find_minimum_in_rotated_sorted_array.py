import pytest

from solutions import (
    FindMinimumRotatedSortedArray,
)


@pytest.fixture
def solution():
    return FindMinimumRotatedSortedArray()


def test_find_minimum_in_rotated_sorted_array(solution):
    nums = [3, 4, 5, 1, 2]
    result = solution.find_min(nums)
    assert result == 1
    nums = [4, 5, 6, 7, 0, 1, 2]
    result = solution.find_min(nums)
    assert result == 0
    nums = [11, 13, 15, 17]
    result = solution.find_min(nums)
    assert result == 11


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = [5001, 5003]
        solution.find_min(nums)

    with pytest.raises(AssertionError):
        nums = [1] * (5001)
        solution.find_min(nums)

    with pytest.raises(AssertionError):
        nums = [1, 1, 1]
        solution.find_min(nums)

    with pytest.raises(AssertionError):
        nums = [4, 3, 2, 1, 5]
        solution.find_min(nums)
