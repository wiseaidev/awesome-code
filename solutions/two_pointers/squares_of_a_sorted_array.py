class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        # Constraints
        length: int = len(nums)
        assert 1 <= length <= 10**4
        for num in nums:
            assert -(10**4) <= num <= 10**4
        assert nums == sorted(nums)
        # Algorithm
        left: int = 0
        right: int = length - 1
        results = [0] * length
        while left <= right:
            abs_left, abs_right = abs(nums[left]), abs(nums[right])
            if abs_left > abs_right:
                results[right - left] = abs_left * abs_left
                left += 1
            else:
                results[right - left] = abs_right * abs_right
                right -= 1
        return results


SquaresOfASortedArray = Solution

__all__ = ["SquaresOfASortedArray"]
