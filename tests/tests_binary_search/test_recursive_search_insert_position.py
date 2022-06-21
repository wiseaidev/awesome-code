import pytest

from solutions import (
    RecursiveSearchInsertPosition,
)


@pytest.fixture
def solution():
    return RecursiveSearchInsertPosition()


def test_iterative_search_insert_position(solution):
    nums = [1, 3, 5, 6]
    result = solution.search_insert(nums, 5)
    assert result == 2
    nums = [1, 3, 5, 6]
    result = solution.search_insert(nums, 2)
    assert result == 1
    nums = [1, 3, 5, 6]
    result = solution.search_insert(nums, 7)
    assert result == 4


def test_constraints(solution):
    with pytest.raises(AssertionError):
        nums = [1] * (10**4 + 1)
        solution.search_insert(nums, 10)

    with pytest.raises(AssertionError):
        nums = [10**4 + 1]
        solution.search_insert(nums, 10)

    with pytest.raises(AssertionError):
        nums = [4, 3, 1, 1, 1]
        solution.search_insert(nums, 1)

    with pytest.raises(AssertionError):
        nums = [4, 3, 2, 1]
        solution.search_insert(nums, 1)

    with pytest.raises(AssertionError):
        nums = [1, 2, 3, 4]
        solution.search_insert(nums, 10**4 + 1)
