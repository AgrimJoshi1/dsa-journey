#Problem No. 118 - Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            r_add = [1] * (i + 1)
            for j in range(1, i):
                r_add[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(r_add)

        return res