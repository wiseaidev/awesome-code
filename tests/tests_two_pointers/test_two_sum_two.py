import pytest

from solutions import (
    TwoSumSolutionTwo,
)


@pytest.fixture
def solution():
    return TwoSumSolutionTwo()


def test_move_zeros_solution_case1(solution):
    nums = [2, 7, 11, 15]
    result = solution.twoSum(nums, 9)
    assert result == [1, 2]


def test_move_zeros_solution_case2(solution):
    nums = [2, 3, 4]
    result = solution.twoSum(nums, 6)
    assert result == [1, 3]


def test_move_zeros_solution_case3(solution):
    nums = [-1, 0]
    result = solution.twoSum(nums, -1)
    assert result == [1, 2]


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = [1]
        solution.twoSum(nums, 0)

    with pytest.raises(AssertionError):
        nums = [0] * 3 * (10**4 + 1)
        solution.twoSum(nums, 0)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4)
        nums[-1] = 1001
        solution.twoSum(nums, 0)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4)
        nums[-1] = 1000
        solution.twoSum(nums, 1001)
