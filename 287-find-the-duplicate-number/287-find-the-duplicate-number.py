class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = set()
        
        for i in nums:
            if i in m:
                return i                
            else:
                m.add(i) 