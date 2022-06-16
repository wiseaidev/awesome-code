from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        stack, ret_list = [], []
        if root:
            stack.append(root)
        else:
            return []
        while stack:
            current = stack.pop()
            if current.val:
                assert -100 <= current.val <= 100
            ret_list.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        assert 0 <= len(ret_list) <= 100
        return ret_list


IterativeBinaryTreeSolution = Solution

__all__ = ["IterativeBinaryTreeSolution"]
