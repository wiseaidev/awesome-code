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
    def average_of_levels(self, root: Optional[TreeNode]) -> list[float]:
        ret_list: list[list[int]] = []
        if not root:
            return ret_list
        # traverse in order level, keeping track of (row number, current node)
        queue = deque()
        # keep track of the nodes in each row
        queue.append(root)
        is_left_to_right = True
        size_of_tree: int = 0
        while queue:
            current_nodes: list[int] = []
            size: int = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.val:
                    assert -(2**31) <= root.val <= 2**31 - 1
                if is_left_to_right:
                    current_nodes.append(node.val)
                else:
                    current_nodes.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            is_left_to_right = not is_left_to_right
            size_of_tree += len(current_nodes)
            ret_list.append(sum(current_nodes) / len(current_nodes))
        # flatten the list
        assert 1 <= size_of_tree <= 104
        return ret_list


AverageOfLevelsOrderTraversalSolution = Solution

__all__ = ["AverageOfLevelsOrderTraversalSolution"]
