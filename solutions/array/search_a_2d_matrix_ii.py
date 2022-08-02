class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        nb_rows, nb_columns = len(matrix), len(matrix[0])
        # Constaints
        assert 1 <= nb_rows <= 300
        assert 1 <= nb_columns <= 300
        for i in range(nb_rows):
            for j in range(nb_columns):
                assert -(10**9) <= matrix[i][j] <= 10**9
                if i == 0:
                    tmp = list(zip(*matrix))
                    assert list(tmp[:][j]) == sorted(list(tmp[:][j]))
            assert matrix[i] == sorted(matrix[i])
        assert -(10**9) <= target <= 10**9
        # Edge Case
        if not nb_rows or not nb_columns:
            return False
        # Algorithm
        bottom, left = nb_rows - 1, 0
        while True:
            if bottom < 0 or left >= nb_columns:
                break
            current: int = matrix[bottom][left]
            if target < current:
                # target is smaller, then go up
                bottom -= 1

            elif target > current:
                # target is larger, then go right
                left += 1

            else:
                # hit target
                return True
        return False


Searcha2DMatrixII = Solution

__all__ = ["Searcha2DMatrixII"]
