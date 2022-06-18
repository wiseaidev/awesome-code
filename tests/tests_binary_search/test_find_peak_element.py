import pytest

from solutions import (
    FindPeakElementSolution,
)


@pytest.fixture
def solution():
    return FindPeakElementSolution()


def test_find_peak_element(solution):
    nums = [1, 2, 3, 1]
    result = solution.find_peak_element(nums)
    assert result == 2
    nums = [1, 2, 1, 3, 5, 6, 4]
    result = solution.find_peak_element(nums)
    assert result == 5


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = [2**31]
        solution.find_peak_element(nums)

    with pytest.raises(AssertionError):
        nums = [1] * (1001)
        solution.find_peak_element(nums)

    with pytest.raises(AssertionError):
        nums = [1, 2, 3, 3, 1]
        solution.find_peak_element(nums)
