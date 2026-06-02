#Problem No. 217 - Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#Approach
#Use a set to keep track of seen numbers. If we encounter a number that is already
#in the set, we return True. If we finish iterating through the array without finding duplicates, we return False.
