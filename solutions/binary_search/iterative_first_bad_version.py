from solutions.binary_search.utils import (
    is_bad_version,
)


class Solution:
    def first_bad_version(self, n: int, bad: int) -> int:
        # Constraints
        assert 1 <= n <= 2**31 - 1
        left: int = 1
        right: int = n
        while left <= right:
            mid: int = left + (right - left) // 2
            if not is_bad_version(mid, bad):
                left = mid + 1
            else:
                right = mid - 1
        return left


IterativeFirstBadVersion = Solution

__all__ = ["IterativeFirstBadVersion"]
