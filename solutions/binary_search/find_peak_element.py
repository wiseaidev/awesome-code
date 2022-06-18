from typing import (
    Optional,
)


class Solution:
    def find_peak_element(self, nums: list[int]) -> int:
        length: int = len(nums)
        assert 1 <= length <= 1000
        for element in nums:
            assert -(2**31) <= element <= 2**31 - 1
        for i in range(length - 1):
            assert nums[i] != nums[i + 1]
        left: int = 0
        right: int = length - 1
        while left < right:
            mid_point: float = left + (right - left) // 2
            if nums[mid_point] < nums[mid_point + 1]:
                left = mid_point + 1
            else:
                right = mid_point
        return left


FindPeakElementSolution = Solution

__all__ = ["FindPeakElementSolution"]
