#Problem No. 12 - Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num
#Approach
#We create two lists, one for the integer values and one for the corresponding Roman numeral symbols
#We iterate through the integer values, and for each value, we check how many times it can fit into the input number
#For each time it fits, we append the corresponding Roman numeral symbol to the result string and
#subtract the value from the input number. We continue this process until we have processed all values.
