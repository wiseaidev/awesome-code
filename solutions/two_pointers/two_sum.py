class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        assert 2 <= len(nums) <= 10**4
        for element in nums:
            assert -(10**9) <= element <= 10**9
        assert -(10**9) <= target <= 10**9
        # sort the array and store it into a tmp variable
        tmp_nums: list[int] = sorted(nums)
        result: list[int] = []
        # declare two pointers left, right
        length: int = len(nums)
        left: int = 0
        right: int = length - 1
        while left < right:
            cur_sum: int = tmp_nums[left] + tmp_nums[right]
            if cur_sum == target:
                result = [
                    nums.index(tmp_nums[left]),
                    length - nums[::-1].index(tmp_nums[right]) - 1,
                ]
                break
            if cur_sum < target:
                left += 1
            else:
                right -= 1
        return result


TwoSumSolution = Solution

__all__ = ["TwoSumSolution"]
