from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> list[int]:
        def helper_one(root: Optional[TreeNode], ret_list: list[int]) -> list[int]:
            if root is None:
                return []
            if root.val:
                assert -100 <= root.val <= 100
            ret_list.append(root.val)
            helper_one(root.left, ret_list)
            helper_one(root.right, ret_list)

        def helper_two(root: Optional[TreeNode]) -> int:
            if root is None:
                return []
            yield root.val
            for value in helper_two(root.left):
                yield value
            for value in helper_two(root.right):
                yield value

        # Base case
        if root is None:
            return []
        ret_list_one: list[int] = []
        ret_list_two: list[int] = []
        helper_one(root, ret_list_one)
        ret_list_two = list(helper_two(root))
        assert 0 <= len(ret_list_one) <= 100
        assert ret_list_one == ret_list_two
        return ret_list_one


RecursiveBinaryTreeSolution = Solution

__all__ = ["RecursiveBinaryTreeSolution"]
