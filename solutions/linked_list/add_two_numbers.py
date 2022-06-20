from typing import (
    Optional,
)

from solutions.linked_list.list_node import (
    ListNode,
)


class Solution:
    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head: ListNode = ListNode(0)
        current_head: ListNode = dummy_head
        carry: int = 0

        while l1 or l2:
            # Get the values from the linkedLists
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)

            # Create a new node with value out, and set it to
            # current node's next, then advance current node to next.
            current_head.next = ListNode(out)
            current_head = current_head.next

            # Move heads to the next node.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        current_head.next = ListNode(carry) if carry > 0 else None

        return dummy_head.next


AddTwoNumbers = Solution

__all__ = ["AddTwoNumbers"]
