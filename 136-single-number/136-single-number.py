class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        
        for i in nums:
            if i not in  m.keys():
                m[i] = 1
            else:
                m[i] += 1
                
        for i in nums:
            if m[i] == 1:
                return i
                