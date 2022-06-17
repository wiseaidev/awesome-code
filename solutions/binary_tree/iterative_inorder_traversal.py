from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        ret_list: list[int] = []
        stack: list[int] = []
        if not root:
            return ret_list

        def push_all_left(root, stack):
            while root:
                if root.val:
                    assert -100 <= root.val <= 100
                stack.append(root)
                root: TreeNode = root.left

        push_all_left(root, stack)
        while len(stack) > 0:
            current: TreeNode = stack.pop()
            ret_list.append(current.val)
            push_all_left(current.right, stack)
        assert 0 <= len(ret_list) <= 100
        return ret_list


IterativeInorderTraversal = Solution

__all__ = ["IterativeInorderTraversal"]
