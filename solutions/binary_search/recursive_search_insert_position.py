class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
        # Constraints
        length: int = len(nums)
        assert 1 <= length <= 10**4
        assert -(10**4) <= target <= 10**4
        for num in nums:
            assert -(10**4) <= num <= 10**4
        assert nums == sorted(nums)
        assert len(set(nums)) == length
        # Algorithm
        ret_val: int = 0
        # Algorithm

        def binary_search(
            nums: list[int], left: int, right: int, target: int, ret_val
        ) -> int:
            if left > right:
                return ret_val
            mid: int = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                return binary_search(nums, left, mid - 1, target, ret_val)
            ret_val = mid + 1
            return binary_search(nums, mid + 1, right, target, ret_val)
            return ret_val

        return binary_search(nums, 0, length - 1, target, ret_val)


RecursiveSearchInsertPosition = Solution

__all__ = ["RecursiveSearchInsertPosition"]
