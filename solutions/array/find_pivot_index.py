class Solution:
    def pivot_index(self, nums: list[int]) -> int:
        length: int = len(nums)
        # Constraints
        assert 1 <= length <= 10**4
        for num in nums:
            assert -1000 <= num <= 1000
        left_sum: int = 0
        right_sum: int = sum(nums)
        for i in range(length):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


FindPivotIndex = Solution

__all__ = ["FindPivotIndex"]
