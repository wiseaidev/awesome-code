from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        ret_list: list[int] = []
        stack: list[int] = []
        if not root:
            return ret_list

        def peek(stack: list[int]) -> Optional[int]:
            if len(stack) > 0:
                return stack[-1]
            return None

        def push_all_right(root: TreeNode, stack: list[int]) -> None:
            while root:
                if root.val:
                    assert -100 <= root.val <= 100
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                # Set root as root's left child
                root = root.left

        push_all_right(root, stack)
        while len(stack) > 0:
            current: "TreeNode" = stack.pop()
            if current.right is not None and peek(stack) == current.right:
                stack.pop()
                stack.append(current)
                current = current.right
            else:
                ret_list.append(current.val)
                current = None
            push_all_right(current, stack)
        assert 0 <= len(ret_list) <= 100
        return ret_list


IterativePostorderTraversal = Solution

__all__ = ["IterativePostorderTraversal"]
