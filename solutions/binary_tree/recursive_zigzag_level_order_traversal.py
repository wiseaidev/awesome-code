from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


class Solution:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
        def helper(
            root: Optional[TreeNode], level: int, ret_list: list[list[int]]
        ) -> None:
            if root:
                if root.val:
                    assert -100 <= root.val <= 100
                if len(ret_list) == level:
                    ret_list.append([])
                direction = 0 if (level % 2) != 0 else len(ret_list[level])
                ret_list[level].insert(direction, root.val)
                helper(root.left, level + 1, ret_list)
                helper(root.right, level + 1, ret_list)

        ret_list: list[list[int]] = []
        if not root:
            return ret_list
        helper(root, 0, ret_list)
        assert 0 <= len([item for sublist in ret_list for item in sublist]) <= 100
        return ret_list


RecursiveZigzagLevelOrderTraversal = Solution

__all__ = ["RecursiveZigzagLevelOrderTraversal"]
