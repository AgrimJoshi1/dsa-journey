#Problem No. 13 - Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        
        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total   
#Approach
# - Create a dictionary to map Roman numerals to their integer values
# - Initialize a variable to store the total value 
# - Iterate through the string, for each character check if it is less than the next character, if it is then subtract its value from the total, otherwise add its value to the total
# - Finally, return the total value which will be the integer representation of the Roman numeral string                    