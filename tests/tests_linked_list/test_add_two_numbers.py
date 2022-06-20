import pytest

from solutions import (
    AddTwoNumbers,
    ListNode,
)
from tests.tests_linked_list.helper import (
    build_linked_list,
)


@pytest.fixture
def solution():
    return AddTwoNumbers()


def test_add_two_numbers_case1(solution):
    l1 = build_linked_list([2, 4, 3])

    l2 = build_linked_list([5, 6, 4])

    ref = build_linked_list([7, 0, 8])

    result = solution.add_two_numbers(l1, l2)
    assert result == ref


def test_add_two_numbers_case2(solution):
    l1 = ListNode(0)

    l2 = ListNode(0)

    ref = ListNode(0)

    result = solution.add_two_numbers(l1, l2)
    assert result == ref


def test_add_two_numbers_case3(solution):
    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])

    l2 = build_linked_list([9, 9, 9, 9])

    ref = build_linked_list([8, 9, 9, 9, 0, 0, 0, 1])

    result = solution.add_two_numbers(l1, l2)
    assert result == ref
