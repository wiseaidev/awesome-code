class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Constraints
        length: int = len(nums)
        assert 1 <= length <= 10**4
        assert -(10**4) < target < 10**4
        for num in nums:
            assert -(10**4) < num < 10**4
        assert nums == sorted(nums)
        assert len(set(nums)) == length
        # Algorithm

        def binary_search(nums: list[int], left: int, right: int, target: int) -> int:
            if left > right:
                return -1
            mid: int = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                return binary_search(nums, left, mid - 1, target)
            return binary_search(nums, mid + 1, right, target)

        return binary_search(nums, 0, length - 1, target)


RecursiveBinarySearch = Solution

__all__ = ["RecursiveBinarySearch"]
