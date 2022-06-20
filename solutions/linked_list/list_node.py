from attrs import (
    define,
)


@define
class ListNode:
    val: int = 0
    next: "ListNode" = None
