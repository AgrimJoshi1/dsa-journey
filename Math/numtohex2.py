#Problem 405. - Number to Hexadecimal
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        result = ""
        num = num & 0xffffffff   
        
        while num > 0:
            rem = num % 16
            result = hex_chars[rem] + result
            num //= 16

        return result
        