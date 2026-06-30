#Problem No. 2570 - Merge 2D Array
class Solution:

    def mergeArrays(self, nums1, nums2):

        d = {}

        for i, val in nums1:
            d[i] = val

        for i, val in nums2:
            if i in d:
                d[i] += val
            else:
                d[i] = val

        l1= []
        for i in sorted(d):
            l1.append([i, d[i]])

        return l1