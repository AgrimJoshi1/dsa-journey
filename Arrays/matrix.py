#Problem No. 3898 - Matrix Diagonal Sum
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        l1 = []
        for i in matrix: 
            c = 0
            for j in i:
                if (j==0):
                    continue 
                else: 
                    c+=1 
            l1.append(c)
        return l1
#Approach
#Declare an empty list and keep on iterating on matrix and for each row declare a counter
#and keep on iterating on each element of row and if element is 0 then continue else add 1 to counter
#Once iteration is complete add counter to list and return list at the end
