class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        
        n = len(nums)//2 +1
        
        for i in nums:
            if m[i] >= n:
                return i