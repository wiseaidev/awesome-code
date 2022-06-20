from typing import (
    Optional,
)

from solutions.linked_list.list_node import (
    ListNode,
)


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Constraints
        dummy_head: ListNode = head
        number_of_nodes: int = 0
        while dummy_head:
            if isinstance(dummy_head.val, int):
                assert -5000 <= dummy_head.val <= 5000
            dummy_head = dummy_head.next
            number_of_nodes += 1
        assert 1 <= number_of_nodes <= 5000
        # Algorithm
        previous: ListNode = None
        while head:
            current: ListNode = head
            head = head.next
            current.next = previous
            previous = current
        return previous


IterativeReverseLinkedList = Solution

__all__ = ["IterativeReverseLinkedList"]
