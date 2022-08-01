from typing import (
    Optional,
)

from solutions.linked_list.list_node import (
    ListNode,
)


class Solution:
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Constraints
        dummy_node1: ListNode = list1
        list_val1: list[int] = []
        dummy_node2: ListNode = list2
        list_val2: list[int] = []
        number_of_nodes: int = 0
        while dummy_node1 and dummy_node2:
            if isinstance(dummy_node1.val, int):
                assert -100 <= dummy_node1.val <= 100
                assert -100 <= dummy_node2.val <= 100
                list_val1.append(dummy_node1.val)
                list_val2.append(dummy_node2.val)
            dummy_node1 = dummy_node1.next
            dummy_node2 = dummy_node2.next
            number_of_nodes += 1
        assert 0 <= number_of_nodes <= 50
        assert list_val1 == sorted(list_val1)
        assert list_val2 == sorted(list_val2)
        # Algorithm

        def helper(
            list1: Optional[ListNode], list2: Optional[ListNode]
        ) -> Optional[ListNode]:
            if not list1 or not list2:
                return list1 or list2
            if list1.val < list2.val:
                list1.next = helper(list1.next, list2)
                return list1
            else:
                list2.next = helper(list1, list2.next)
                return list2

        return helper(list1, list2)


RecursiveMergeTwoSortedLists = Solution

__all__ = ["RecursiveMergeTwoSortedLists"]
