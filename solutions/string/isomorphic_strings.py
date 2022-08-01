class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        s_length: int = len(s)
        t_length: int = len(t)
        # Constraints
        assert 1 <= s_length <= 5 * 10**4
        assert t_length == s_length
        # Algorithm
        chars_dict = {}
        for s_char, t_char in zip(s, t):
            values: list[str] = chars_dict.values()
            if s_char not in chars_dict and t_char not in values:
                chars_dict[s_char] = t_char
            if s_char not in chars_dict and t_char in values:
                return False
            if s_char in chars_dict and chars_dict[s_char] is not t_char:
                return False

        return True


IsomorphicStrings = Solution

__all__ = [
    "IsomorphicStrings",
]
