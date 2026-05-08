#Problem No. 387 First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1