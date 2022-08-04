import pytest

from solutions import (
    MedianofTwoSortedArrays,
)


@pytest.fixture
def solution():
    return MedianofTwoSortedArrays()


def test_find_median_sorted_arrays_case_1(solution):
    nums1 = [1, 3]
    nums2 = [2]
    ref = 2.0
    assert ref == solution.find_median_sorted_arrays(nums1, nums2)


def test_find_median_sorted_arrays_case_2(solution):
    nums1 = [1, 2]
    nums2 = [3, 4]
    ref = 2.5
    assert ref == solution.find_median_sorted_arrays(nums1, nums2)


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums1 = [1] * 1001
        nums2 = [2] * 99
        solution.find_median_sorted_arrays(nums1, nums2)

    with pytest.raises(AssertionError):
        nums1 = [1] * 99
        nums2 = [2] * 1001
        solution.find_median_sorted_arrays(nums1, nums2)

    with pytest.raises(AssertionError):
        nums1 = [1] * 1001
        nums2 = [2] * 1001
        solution.find_median_sorted_arrays(nums1, nums2)

    with pytest.raises(AssertionError):
        nums1 = [10**6 + 1] * 5
        nums2 = [3, 4]
        solution.find_median_sorted_arrays(nums1, nums2)
