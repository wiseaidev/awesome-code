from typing import (
    Optional,
)

from solutions.linked_list.list_node import (
    ListNode,
)


class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Constraints
        dummy_head: ListNode = head
        number_of_nodes: int = 0
        while dummy_head:
            if isinstance(dummy_head.val, int):
                assert 1 <= dummy_head.val <= 1000
            dummy_head = dummy_head.next
            number_of_nodes += 1
        assert 1 <= number_of_nodes <= 5 * 10**4
        # Algorithm
        # step 1: find middle
        if not head:
            return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        # step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt


ReorderList = Solution

__all__ = ["ReorderList"]
