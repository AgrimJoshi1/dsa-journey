#Problem No. 14- Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for j in strs[1:]:
                if i >= len(j) or j[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]