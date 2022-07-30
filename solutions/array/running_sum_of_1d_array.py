class Solution:
    def running_sum(self, nums: list[int]) -> list[int]:
        length: int = len(nums)
        # Constraints
        assert 1 <= length <= 1000
        for num in nums:
            assert -(10**6) <= num <= 10**6
        # Algorithm
        for i in range(1, length):
            nums[i] += nums[i - 1]
        return nums


RunningSumOfArray = Solution

__all__ = ["RunningSumOfArray"]
