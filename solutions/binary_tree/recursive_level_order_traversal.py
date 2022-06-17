from collections import (
    deque,
)
from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
        def helper(node: Optional[TreeNode], level: int, ret_list: list[list[int]]):
            if not node:
                return

            if node.val:
                assert -100 <= root.val <= 100
            if level > len(ret_list):
                ret_list.append([node.val])
            else:
                ret_list[level - 1].extend([node.val])

            helper(node.left, level + 1, ret_list)
            helper(node.right, level + 1, ret_list)

        if not root:
            return []

        ret_list: list[list[int]] = []
        helper(root, 1, ret_list)
        assert 0 <= len([item for sublist in ret_list for item in sublist]) <= 100
        return ret_list


RecursiveLevelOrderTraversal = Solution

__all__ = ["RecursiveLevelOrderTraversal"]
