#Problem No. 1
'''TWO SUM'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}

        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i

# Approach:
# - Use a dictionary to store value -> index
# - For each element, check if (target - current element) already exists (key value pair)
# - If yes, we found the pair