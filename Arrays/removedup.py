#Problem No. 26 - Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
#Approach
#Use two pointers, one for iterating through the array and another for keeping track of the
