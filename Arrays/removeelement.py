#Problem No. 27 - Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
#Approach
#Use two pointers to iterate through the list. The first pointer (i) keeps track of
#the position of the next non-val element, while the second pointer (j) iterates through the list.
#If the current element (nums[j]) is not equal to val, we copy it to
#the position of the first pointer (nums[i]) and increment the first pointer (i).
#Finally, we return the value of the first pointer (i), which represents the new length
#of the modified list