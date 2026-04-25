#Problem No. 344 - Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
#Approach
#Use two pointers, one starting at the beginning of the list and the other starting at the
#end of the list. Swap the characters at the two pointers and move the pointers towards each other until they meet.