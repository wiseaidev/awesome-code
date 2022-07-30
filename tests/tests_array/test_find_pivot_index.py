import pytest

from solutions import (
    FindPivotIndex,
)


@pytest.fixture
def solution():
    return FindPivotIndex()


def test_pivot_index_case1(solution):
    nums = [1, 7, 3, 6, 5, 6]
    ref = 3
    result = solution.pivot_index(nums)
    assert ref == result


def test_pivot_index_case2(solution):
    nums = [1, 2, 3]
    ref = -1
    result = solution.pivot_index(nums)
    assert ref == result


def test_pivot_index_case3(solution):
    nums = [2, 1, -1]
    ref = 0
    result = solution.pivot_index(nums)
    assert ref == result


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = []
        solution.pivot_index(nums)

    with pytest.raises(AssertionError):
        nums = [4] * (10001)
        solution.pivot_index(nums)

    with pytest.raises(AssertionError):
        nums = [0] * (10**6)
        nums[-1] = 1001
        solution.pivot_index(nums)
