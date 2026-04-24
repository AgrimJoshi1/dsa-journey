#Problem No. 58 - Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        return len(word[-1])
#Approach
#Split the string into a list of words and return the length of the last word in the list.
