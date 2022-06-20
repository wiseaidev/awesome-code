from solutions import (
    ListNode,
)


def build_linked_list(list_):
    current_head = dummy_head = ListNode(0)
    for element in list_:
        current_head.next = ListNode(element)
        current_head = current_head.next
    return dummy_head.next
