import pytest

from solutions import (
    MoveZerosSolution,
)


@pytest.fixture
def solution():
    return MoveZerosSolution()


def test_move_zeros_solution_case1(solution):
    nums = [0, 1, 0, 3, 12]
    # list is passed by reference
    solution.move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_move_zeros_solution_case2(solution):
    nums = [0]
    # list is passed by reference
    solution.move_zeroes(nums)
    assert nums == [0]


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = []
        solution.move_zeroes(nums)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4 + 1)
        solution.move_zeroes(nums)

    with pytest.raises(AssertionError):
        nums = [0] * (10**4)
        nums[-1] = 10**31
        solution.move_zeroes(nums)
