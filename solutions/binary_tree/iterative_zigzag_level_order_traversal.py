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
    def zigzag_level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
        ret_list: list[list[int]] = []
        if not root:
            return ret_list
        queue = deque()
        queue.append(root)
        is_left_to_right: bool = True
        while queue:
            current_nodes: list[int] = []
            size: int = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.val:
                    assert -100 <= root.val <= 100
                if is_left_to_right:
                    current_nodes.append(node.val)
                else:
                    current_nodes.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            is_left_to_right = not is_left_to_right
            ret_list.append(current_nodes)
        assert 0 <= len([item for sublist in ret_list for item in sublist]) <= 2000
        return ret_list


ZigzagLevelOrderTraversal = Solution

__all__ = ["ZigzagLevelOrderTraversal"]
