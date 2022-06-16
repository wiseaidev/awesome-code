from attrs import (
    define,
)


@define
class TreeNode:
    val: int = 0
    left: "TreeNode" = None
    right: "TreeNode" = None
