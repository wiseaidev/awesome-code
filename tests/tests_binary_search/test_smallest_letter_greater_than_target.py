import pytest

from solutions import (
    SmallestLetterGreaterThanTarget,
)


@pytest.fixture
def solution():
    return SmallestLetterGreaterThanTarget()


def test_smallest_letter_greater_than_target(solution):
    letters = ["c", "f", "j"]
    result = solution.next_greatest_letter(letters, "a")
    assert result == "c"
    result = solution.next_greatest_letter(letters, "c")
    assert result == "f"
    result = solution.next_greatest_letter(letters, "d")
    assert result == "f"


def test_constraints(solution):
    with pytest.raises(AssertionError):
        letters = ["c", "c"]
        solution.next_greatest_letter(letters, "c")

    with pytest.raises(AssertionError):
        letters = ["c"] * (2**4 + 1)
        solution.next_greatest_letter(letters, "c")

    with pytest.raises(AssertionError):
        letters = ["c", "b", "a"]
        solution.next_greatest_letter(letters, "c")

    with pytest.raises(AssertionError):
        letters = ["c", "b", "a"]
        solution.next_greatest_letter(letters, "D")

    with pytest.raises(AssertionError):
        letters = ["c", "b", "D"]
        solution.next_greatest_letter(letters, "c")
