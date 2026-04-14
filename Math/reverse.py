#Problem No. 7 - Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x>0: 
            last_digit = x%10 
            rev = (rev*10) + last_digit
            x //= 10
        rev *= sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
#Approach
# - Use a variable to store the reversed number and a variable to store the sign of the number
# - Use a while loop to extract the last digit of the number and add it to the reversed number
# - Update the original number by removing the last digit
# - Finally, check if the reversed number is within the 32-bit signed integer range, if not return 0, else return the reversed number with the correct sign.