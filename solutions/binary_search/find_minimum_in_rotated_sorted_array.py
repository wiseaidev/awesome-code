from typing import (
    Optional,
)


class Solution:
    def find_min(self, nums: list[int]) -> int:
        length: int = len(nums)
        assert 1 <= length <= 5000
        for element in nums:
            assert -5000 <= element <= 5000
        assert len(set(nums)) == length
        rotated: int = 0
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                rotated += 1
        assert rotated == 1 or sorted(nums) == nums
        left: int = 0
        right: int = length - 1
        # edge case: sorted and not rotated
        if not rotated:
            return nums[left]
        while left < right:
            mid_point: float = left + (right - left) // 2
            if nums[mid_point] > nums[right]:
                left = mid_point + 1
            else:
                right = mid_point
        return min(nums[left], nums[right])


FindMinimumRotatedSortedArray = Solution

__all__ = ["FindMinimumRotatedSortedArray"]
