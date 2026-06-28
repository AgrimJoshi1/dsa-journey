#Problem No. 191 - Number of 1 Bits
class Solution(object):
    def hammingWeight(self, n):
        count = 0

        while n:
            count += 1
            n = n & (n - 1)
        return count