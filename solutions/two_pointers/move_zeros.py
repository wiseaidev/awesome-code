class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        assert 1 <= len(nums) <= 10**4
        for element in nums:
            assert -(10**31) <= element <= 10**31 - 1
        length: int = len(nums)
        left: int = 0
        right: int = left + 1
        if length >= 2:
            while right < length:
                if nums[left] != 0:
                    left += 1
                if nums[left] == 0 and nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                right += 1


MoveZerosSolution = Solution

__all__ = [
    "MoveZerosSolution",
]
