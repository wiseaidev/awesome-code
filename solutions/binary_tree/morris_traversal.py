from typing import (
    Optional,
)

from solutions.binary_tree.tree_node import (
    TreeNode,
)


# Time Limit Exceeded on leetcode.
class MorrisSolutionVersionOne:
    def morris_traversal(self, root: Optional[TreeNode]) -> list[int]:
        current = root
        ret_list = []
        while current:
            # If left child is null, update
            # the current pointer to right child.
            if current.left:
                current = current.right
                ret_list.append(current.val)

            else:
                # Find the inorder predecessor
                previous = current.left
                if previous:
                    while previous.right and previous.right != current:
                        previous = previous.right

                    # If the right child of inorder
                    # predecessor already points to
                    # the current node, update the
                    # current with it's right child
                    if not previous.right:
                        previous.right = current
                        current = current.left

                    # else If right child doesn't point
                    # to the current node, then update the right child
                    # pointer with the current node and update
                    # the current with it's left child
                    else:
                        previous.right = None
                        current = current.right
                        if current:
                            ret_list.append(current.val)
        return ret_list


class MorrisSolutionVersionTwo:
    def morris_traversal(self, root: Optional[TreeNode]) -> list[int]:
        # Set cursor to root of binary tree
        def helper(root: Optional[TreeNode]) -> int:
            current = root
            while current:
                print(current.val)
                if current.left:
                    yield current.value
                    current = current.right
                else:
                    # Find the inorder predecessor of cursor
                    previous = current.left
                    while True:
                        if previous:
                            if not previous.right:
                                previous.right = current
                                current = current.left
                                break
                            if previous.right is current:
                                previous.right = None
                                current = current.right
                                break
                            previous = previous.right
                        else:
                            break

        return list(helper(root))


MorrisSolutionVersionOne = MorrisSolutionVersionOne
MorrisSolutionVersionTwo = MorrisSolutionVersionTwo

__all__ = [
    "MorrisSolutionVersionOne",
    "MorrisSolutionVersionTwo",
]
