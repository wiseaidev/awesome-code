from typing import (
    Optional,
)


class Solution:
    def next_greatest_letter(self, letters: list[str], target: str) -> str:
        length: int = len(letters)
        assert 2 <= length <= 10**4
        for letter in letters:
            assert "a" <= letter and target <= "z"
        assert sorted(letters) == letters
        assert len(letters) == len(set(letters))
        assert len(set(letters)) >= 2
        if letters[-1] <= target or letters[0] > target:
            return letters[0]
        left: int = 0
        right: int = length - 1
        while left <= right:
            mid_point: float = left + (right - left) // 2
            if letters[mid_point] > target:
                right = mid_point - 1
            else:
                left = mid_point + 1
        return letters[left]


SmallestLetterGreaterThanTarget = Solution

__all__ = ["SmallestLetterGreaterThanTarget"]
