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
        current = dummy = ListNode()
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
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2

        if list1 or list2:
            current.next = list1 if list1 else list2

        return dummy.next


IterativeMergeTwoSortedLists = Solution

__all__ = ["IterativeMergeTwoSortedLists"]
