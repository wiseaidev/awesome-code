import pytest

from solutions import (
    RecursiveFirstBadVersion,
)


@pytest.fixture
def solution():
    return RecursiveFirstBadVersion()


def test_iterative_first_bad_version(solution):
    result = solution.first_bad_version(5, 4)
    assert result == 4
    result = solution.first_bad_version(1, 1)
    assert result == 1


def test_constraints(solution):
    with pytest.raises(AssertionError):
        solution.first_bad_version(2**31, 1)
