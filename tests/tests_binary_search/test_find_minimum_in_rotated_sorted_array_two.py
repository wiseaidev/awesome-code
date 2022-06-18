import pytest

from solutions import (
    FindMinimumRotatedSortedArrayTwo,
)


@pytest.fixture
def solution():
    return FindMinimumRotatedSortedArrayTwo()


def test_find_minimum_in_rotated_sorted_array_two(solution):
    nums = [1, 3, 5]
    result = solution.find_min(nums)
    assert result == 1
    nums = [2, 2, 2, 0, 1]
    result = solution.find_min(nums)
    assert result == 0
    nums = [12, 1, 12, 12, 12]
    result = solution.find_min(nums)
    assert result == 1


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = [5001, 5003]
        solution.find_min(nums)

    with pytest.raises(AssertionError):
        nums = [1] * (5001)
        solution.find_min(nums)
