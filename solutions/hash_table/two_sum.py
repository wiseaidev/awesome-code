class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # constaints
        assert 2 <= len(nums) <= 10**4
        for element in nums:
            assert -(10**9) <= element <= 10**9
        assert -(10**9) <= target <= 10**9
        # key: number seen in the list, val: index of that element
        seen_nums: dict[int, int] = {}
        result: list[int] = []
        for index, element in enumerate(nums):
            difference: int = target - element
            if difference in seen_nums:
                result = [seen_nums.get(difference, -1), index]
                break
            else:
                seen_nums[element] = index
        return result


TwoSumHashTableSolution = Solution

__all__ = ["TwoSumHashTableSolution"]
