class Solution(object):
    def longestPalindrome(self, s):
        x = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                y = s[i:j+1]

                if y == y[::-1]:
                    if len(y) > len(x):
                        x = y

        return x