#Problem No 1662 - Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s1=""
        s2=""
        for i in word1:
            s1+=i
        for i in word2:
            s2+=i
        if s1==s2:
            return True 
        else:
            return False
#Approach 
#Declare two empty strings and keep iterating on word1, word2 and keep on adding letters to strings
#Once iteration is complete check if both string are equal then return True
