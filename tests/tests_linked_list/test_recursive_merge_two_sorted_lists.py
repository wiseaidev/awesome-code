import pytest

from solutions import (
    ListNode,
    RecursiveMergeTwoSortedLists,
)
from tests.tests_linked_list.helper import (
    build_linked_list,
)


@pytest.fixture
def solution():
    return RecursiveMergeTwoSortedLists()


def test_merge_two_lists_case1(solution):
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])

    ref = build_linked_list([1, 1, 2, 3, 4, 4])

    result = solution.merge_two_lists(list1, list2)
    assert result == ref


def test_merge_two_lists_case2(solution):
    list1 = build_linked_list([])
    list2 = build_linked_list([])

    ref = build_linked_list([])

    result = solution.merge_two_lists(list1, list2)
    assert result == ref


def test_merge_two_lists_case3(solution):
    list1 = build_linked_list([])
    list2 = build_linked_list([0])

    ref = build_linked_list([0])

    result = solution.merge_two_lists(list1, list2)
    assert result == ref


def test_constraints(solution):
    with pytest.raises(AssertionError):
        list1 = build_linked_list([1] * 51)
        list2 = build_linked_list([1] * 51)
        solution.merge_two_lists(list1, list2)

    with pytest.raises(AssertionError):
        list1 = build_linked_list([101] * 50)
        list2 = build_linked_list([100] * 50)
        solution.merge_two_lists(list1, list2)

    with pytest.raises(AssertionError):
        list1 = build_linked_list([1, 4, 1])
        list2 = build_linked_list([1, 2, 3])
        solution.merge_two_lists(list1, list2)
