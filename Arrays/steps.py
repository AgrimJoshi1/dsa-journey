#Problem No. 70 - Steps
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2

        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
            
        return b

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
