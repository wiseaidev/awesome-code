import pytest

from solutions import (
    TwoSumSolution,
)


@pytest.fixture
def solution():
    return TwoSumSolution()


def test_move_zeros_solution_case1(solution):
    nums = [2, 7, 11, 15]
    result = solution.twoSum(nums, 9)
    assert result == [0, 1]


def test_move_zeros_solution_case2(solution):
    nums = [3, 2, 4]
    result = solution.twoSum(nums, 6)
    assert result == [1, 2]


def test_move_zeros_solution_case3(solution):
    nums = [3, 3]
    result = solution.twoSum(nums, 6)
    assert result == [0, 1]


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = [1]
        solution.twoSum(nums, 6)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4 + 1)
        solution.twoSum(nums, 0)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4)
        solution.twoSum(nums, 10**9 + 1)
