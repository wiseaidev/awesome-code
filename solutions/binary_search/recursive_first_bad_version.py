from solutions.binary_search.utils import (
    is_bad_version,
)


class Solution:
    def first_bad_version(self, n: int, bad: int) -> int:
        # Constraints
        assert 1 <= n <= 2**31 - 1
        # Algorithm

        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            if left == right:
                return left
            mid: int = left + (right - left) // 2
            if not is_bad_version(mid, bad):
                return binary_search(mid + 1, right)
            return binary_search(left, mid)

        return binary_search(1, n)


RecursiveFirstBadVersion = Solution

__all__ = ["RecursiveFirstBadVersion"]
