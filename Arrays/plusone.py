#Problem No. 66 - Plus One
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=""
        for i in digits:
            s+=str(i)
        s=str(int(s)+1)
        res=[]
        for i in s:
            res.append(int(i))
        return res
#Approach
#Declare an empty string and keep on iterating on digits and keep on adding numbers to string
#Once iteration is complete convert string to integer and add 1 to it and then convert it
#back to string and then iterate on string and add each number to result list and return result list
