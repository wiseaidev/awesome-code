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
        left: int = 0
        right: int = length - 1
        while left <= right:
            mid: int = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


IterativeBinarySearch = Solution

__all__ = ["IterativeBinarySearch"]
