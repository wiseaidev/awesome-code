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
        stack: list[ListNode] = []
        node: ListNode = head
        if not head:
            return None
        while node:
            stack.append(node)
            node = node.next
        new_head = stack.pop()
        node = new_head
        while stack:
            node.next = stack.pop()
            node = node.next
        node.next = None
        return new_head


StackIterativeReverseLinkedList = Solution

__all__ = ["StackIterativeReverseLinkedList"]
