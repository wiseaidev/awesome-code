class Solution:
    def kth_smallest(self, matrix: list[list[int]], k: int) -> int:
        nb_rows, nb_columns = len(matrix), len(matrix[0])
        assert nb_rows == nb_columns
        assert 1 <= nb_rows <= 300
        for i in range(nb_rows):
            for j in range(nb_columns):
                assert -(10**9) <= matrix[i][j] <= 10**9
                if i == 0:
                    tmp = list(zip(*matrix))
                    assert list(tmp[:][j]) == sorted(list(tmp[:][j]))
            assert matrix[i] == sorted(matrix[i])
        assert 1 <= k <= nb_rows**2

        def countLessOrEqual(value):
            count: int = 0
            right: int = nb_rows - 1  # start with the rightmost column
            for j in range(nb_columns):
                while right >= 0 and matrix[j][right] > value:
                    right -= 1  # decrease column until matrix[j][right] <= value
                count += right + 1
            return count

        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1  # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side

        return ans


KthSmallestElementInASortedMatrix = Solution

__all__ = ["KthSmallestElementInASortedMatrix"]
