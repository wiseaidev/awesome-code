import pytest

from solutions import (
    ListNode,
    ReorderList,
)
from tests.tests_linked_list.helper import (
    build_linked_list,
)


@pytest.fixture
def solution():
    return ReorderList()


def test_reorder_list_case1(solution):
    head = build_linked_list([1, 2, 3, 4])

    ref = build_linked_list([1, 4, 2, 3])

    solution.reorder_list(head)
    assert head == ref


def test_reorder_list_case2(solution):
    head = build_linked_list([1, 2, 3, 4, 5])

    ref = build_linked_list([1, 5, 2, 4, 3])

    solution.reorder_list(head)
    assert head == ref


def test_reorder_list_case3(solution):
    head = build_linked_list([])

    ref = build_linked_list([])

    assert head == ref


def test_constraints(solution):
    with pytest.raises(AssertionError):
        head = build_linked_list([1] * 50001)
        solution.reorder_list(head)

    with pytest.raises(AssertionError):
        head = build_linked_list([1001])
        solution.reorder_list(head)
