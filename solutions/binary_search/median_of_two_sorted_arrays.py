class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Constraints
        m, n = len(nums1), len(nums2)
        assert 0 <= m <= 1000
        assert 0 <= n <= 1000
        assert 0 <= m + n <= 1000
        for num1 in nums1:
            assert -(10**6) <= num1 <= 10**6
        for num2 in nums2:
            assert -(10**6) <= num2 <= 10**6
        # Algorithm
        # Make sure to perform binary search on the smaller array.
        if len(nums1) > len(nums2):
            return self.find_median_sorted_arrays(nums2, nums1)

        INT_MIN, INT_MAX = -(2**64), 2**64

        # Setup left and right pointers
        left, right = 0, len(nums1)
        left_partition_size = (len(nums1) + len(nums2) + 1) // 2
        n = len(nums1) + len(nums2)

        while left <= right:

            # Get the paritions of both arrays
            p1 = (left + right) // 2
            p2 = left_partition_size - p1

            # Get the 4 boundary numbers
            nums1_leftmost = nums1[p1 - 1] if p1 > 0 else INT_MIN
            nums1_rightmost = nums1[p1] if p1 < len(nums1) else INT_MAX

            nums2_leftmost = nums2[p2 - 1] if p2 > 0 else INT_MIN
            nums2_rightmost = nums2[p2] if p2 < len(nums2) else INT_MAX

            # Move the right pointer to p1
            if nums1_leftmost > nums2_rightmost:
                right = p1 - 1

            # Move the left pointer to p1
            elif nums2_leftmost > nums1_rightmost:
                left = p1 + 1

            # Found the correct parition
            else:

                # Odd length
                if n % 2 == 1:
                    return max(nums1_leftmost, nums2_leftmost)

                # even length
                return (
                    max(nums1_leftmost, nums2_leftmost)
                    + min(nums1_rightmost, nums2_rightmost)
                ) / 2


MedianofTwoSortedArrays = Solution

__all__ = ["MedianofTwoSortedArrays"]
