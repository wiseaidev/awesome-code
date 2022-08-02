import pytest

from solutions import (
    KthSmallestElementInASortedMatrix,
)


@pytest.fixture
def solution():
    return KthSmallestElementInASortedMatrix()


def test_kth_smallest_case1(solution):
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    ref = 13
    result = solution.kth_smallest(matrix, 8)
    assert ref == result


def test_kth_smallest_case2(solution):
    matrix = [[-5]]
    ref = -5
    result = solution.kth_smallest(matrix, 1)
    assert ref == result


def test_constraints(solution):
    with pytest.raises(AssertionError):
        matrix = [[1] * 301]
        solution.kth_smallest(matrix, 2)

    with pytest.raises(AssertionError):
        matrix = [[1] * 300]
        solution.kth_smallest(matrix, 10**9 + 1)

    with pytest.raises(AssertionError):
        matrix = [[10**9 + 1] * 300]
        solution.kth_smallest(matrix, 2)

    with pytest.raises(AssertionError):
        matrix = [[10**9] * 300]
        solution.kth_smallest(matrix, 0)
