from attrs import (
    define,
)


@define
class Node:
    val: int = 0
    left: "Node" = None
    right: "Node" = None
    next: "Node" = None
