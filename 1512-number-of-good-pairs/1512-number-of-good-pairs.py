class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}
        
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] +=1
        c = 0 
        for i in m:
            if m[i] >1:
                c += (m[i]*(m[i]-1))//2
        
        return c
                
        