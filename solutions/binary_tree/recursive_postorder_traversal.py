from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        ret_list: list[int] = []
        if not root:
            return ret_list

        def helper(root: TreeNode, ret_list: list[int]) -> None:
            if not root:
                return
            if root.val:
                assert -100 <= root.val <= 100
            helper(root.left, ret_list)
            helper(root.right, ret_list)
            ret_list.append(root.val)

        helper(root, ret_list)
        assert 0 <= len(ret_list) <= 100
        return ret_list


RecursivePostorderTraversal = Solution

__all__ = ["RecursivePostorderTraversal"]
