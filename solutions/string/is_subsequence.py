class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        s_length: int = len(s)
        t_length: int = len(t)
        # Constraints
        assert 0 <= s_length <= 100
        assert 0 <= t_length <= 10**4
        # Algorithm
        i: int = 0
        for char in t:
            if i == s_length:
                break
            if s[i] == char:
                i += 1
        return i == s_length


IsSubsequence = Solution

__all__ = [
    "IsSubsequence",
]
