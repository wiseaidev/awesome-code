class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # constaints
        assert 2 <= len(nums) <= 3 * 10**4
        for element in nums:
            assert -1000 <= element <= 1000
        assert sorted(nums) == nums
        assert -1000 <= target <= 1000
        # the array is sorted
        result: list[int] = []
        # declare two pointers left, right
        length: int = len(nums)
        left: int = 0
        right: int = length - 1
        while left < right:
            cur_sum: int = nums[left] + nums[right]
            if cur_sum == target:
                result = [left + 1, right + 1]
                break
            if cur_sum < target:
                left += 1
            else:
                right -= 1
        return result


TwoSumSolutionTwo = Solution

__all__ = ["TwoSumSolutionTwo"]
