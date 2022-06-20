import pytest

from solutions import (
    ListNode,
    RecursiveReverseLinkedList,
)
from tests.tests_linked_list.helper import (
    build_linked_list,
)


@pytest.fixture
def solution():
    return RecursiveReverseLinkedList()


def test_reverse_list_case1(solution):
    head = build_linked_list([1, 2, 3, 4, 5])

    ref = build_linked_list([5, 4, 3, 2, 1])

    result = solution.reverse_list(head)
    assert result == ref


def test_reverse_list_case2(solution):
    head = ListNode([])

    ref = ListNode([])

    result = solution.reverse_list(head)
    assert result == ref


def test_reverse_list_case3(solution):
    head = build_linked_list([1, 2])

    ref = build_linked_list([2, 1])

    result = solution.reverse_list(head)
    assert result == ref


def test_constraints(solution):
    with pytest.raises(AssertionError):
        head = build_linked_list([1] * 5001)
        solution.reverse_list(head)

    with pytest.raises(AssertionError):
        head = build_linked_list([5001])
        solution.reverse_list(head)
