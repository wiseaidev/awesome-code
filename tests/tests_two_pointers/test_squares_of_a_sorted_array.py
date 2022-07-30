import pytest

from solutions import (
    SquaresOfASortedArray,
)


@pytest.fixture
def solution():
    return SquaresOfASortedArray()


def test_move_zeros_solution_case1(solution):
    nums = [-4, -1, 0, 3, 10]
    result = solution.sorted_squares(nums)
    assert result == [0, 1, 9, 16, 100]


def test_move_zeros_solution_case2(solution):
    nums = [-7, -3, 2, 3, 11]
    result = solution.sorted_squares(nums)
    assert result == [4, 9, 9, 49, 121]


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = []
        solution.sorted_squares(nums)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4 + 1)
        solution.sorted_squares(nums)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4)
        nums[-1] = 10**4 + 1
        solution.sorted_squares(nums)

    with pytest.raises(AssertionError):
        nums = [3, 2, 1]
        solution.sorted_squares(nums)
