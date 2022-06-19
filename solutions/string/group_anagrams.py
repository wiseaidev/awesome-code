from collections import (
    defaultdict,
)


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        assert 1 <= len(strs) <= 10**4
        for string in strs:
            assert 0 <= len(string) <= 100
            assert string.lower() == string
        result = defaultdict(list)
        for string in strs:
            result["".join(sorted(string))].append(string)
        return list(result.values())


GroupAnagrams = Solution

__all__ = [
    "GroupAnagrams",
]
