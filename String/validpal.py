#Problem No. 125 - Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for i in s:
            if i.isalnum():      
                pal += i.lower()
        return pal == pal[::-1]
#Approach 
#Empty list initialised
#iterate through main list, isalnum() removes all the alpha numeric items and cleans list
#check if final list is same, return true
