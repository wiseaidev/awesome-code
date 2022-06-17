from collections import (
    deque,
)
from typing import (
    Optional,
)

from solutions.binary_tree.node import (
    Node,
)


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        # traverse in order level, keeping track of (row number, current node)
        queue = deque()
        # keep track of the nodes in each row
        queue.append(root)

        while queue:
            previous = None
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if previous:
                    previous.next = current
                # make previous node as current
                previous = current
                if current.left:
                    queue.append(current.left)
                    queue.append(current.right)

        return root


PopulatingNextRightPointersSolution = Solution

__all__ = ["PopulatingNextRightPointersSolution"]
