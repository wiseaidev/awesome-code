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
        ret_list: list[list[int]] = []
        if not root:
            return ret_list
        # traverse in order level, keeping track of (row number, current node)
        queue = deque()
        # keep track of the nodes in each row
        queue.append(root)

        while queue:
            current_nodes: list[int] = []
            size: int = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.val:
                    assert -1000 <= root.val <= 1000
                current_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret_list.append(current_nodes)
        # flatten the list
        assert 0 <= len([item for sublist in ret_list for item in sublist]) <= 100
        return ret_list


LevelOrderTraversalSolution = Solution

__all__ = ["LevelOrderTraversalSolution"]
