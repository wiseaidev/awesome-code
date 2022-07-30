import pytest

from solutions import (
    RunningSumOfArray,
)


@pytest.fixture
def solution():
    return RunningSumOfArray()


def test_running_sum_case1(solution):
    nums = [1, 2, 3, 4]
    ref = [1, 3, 6, 10]
    result = solution.running_sum(nums)
    assert ref == result


def test_running_sum_case2(solution):
    nums = [1, 1, 1, 1, 1]
    ref = [1, 2, 3, 4, 5]
    result = solution.running_sum(nums)
    assert ref == result


def test_running_sum_case3(solution):
    nums = [3, 1, 2, 10, 1]
    ref = [3, 4, 6, 16, 17]
    result = solution.running_sum(nums)
    assert ref == result


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = []
        solution.running_sum(nums)

    with pytest.raises(AssertionError):
        nums = [4] * (1001)
        solution.running_sum(nums)

    with pytest.raises(AssertionError):
        nums = [0] * (10**6)
        nums[-1] = 10**6 + 1
        solution.running_sum(nums)
