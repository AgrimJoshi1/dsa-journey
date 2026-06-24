#Problem No. 136 - Single Number
class Solution(object):
    def singleNumber(self, nums):
        lst = []

        for num in nums:
            if num in lst:
                lst.remove(num)
            else:
                lst.append(num)

        return lst[0]
