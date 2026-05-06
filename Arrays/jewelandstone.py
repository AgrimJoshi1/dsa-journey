#Problem No. 771 - Jewels And Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set()
        for i in jewels: 
            jset.add(i)
        
        count = 0
        for i in stones:
            if i in jset: 
                count+=1
        return count
#Approach 
#Using set because searching in set() is faster as for a list, it checks every entity one by one