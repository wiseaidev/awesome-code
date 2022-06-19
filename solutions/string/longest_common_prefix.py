class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        length: int = len(strs)
        if length < 1:
            return ""
        assert 1 <= length <= 200
        for string in strs:
            assert 0 <= len(string) <= 200
            assert string == string.lower()
        common_prefix: str = strs[0]
        for index in range(1, length):
            while not strs[index].startswith(common_prefix):
                common_prefix = common_prefix[:-1]
        return common_prefix


LongestCommonPrefix = Solution

__all__ = [
    "LongestCommonPrefix",
]
