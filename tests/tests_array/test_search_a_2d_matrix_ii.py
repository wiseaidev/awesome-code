import pytest

from solutions import (
    Searcha2DMatrixII,
)


@pytest.fixture
def solution():
    return Searcha2DMatrixII()


def test_search_matrix_case(solution):
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    ref = False
    result = solution.search_matrix(matrix, 20)
    assert ref == result


def test_constraints(solution):
    with pytest.raises(AssertionError):
        matrix = [[1] * 301]
        solution.search_matrix(matrix, 2)

    with pytest.raises(AssertionError):
        matrix = [[1] * 300]
        solution.search_matrix(matrix, 10**9 + 1)

    with pytest.raises(AssertionError):
        matrix = [[10**9 + 1] * 300]
        solution.search_matrix(matrix, 2)
