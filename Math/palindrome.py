#Problem No. 9 - Palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        a = x
        rev = 0

        while a > 0:
            r = a % 10
            rev = rev * 10 + r
            a = a // 10

        return x == rev
#Approach
#using basic math function, first divide by 10 to get last digit then repeat and keep on adding the remainder 
#once iteration is complete compare with the original if same then palindrome
