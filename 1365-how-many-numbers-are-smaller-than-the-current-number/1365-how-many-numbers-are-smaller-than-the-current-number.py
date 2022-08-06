class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = sorted(nums)
        m = {}
        for i in range(len(nums)):
            if x[i] not in m:
                m[x[i]] = i
                
        for i in range(len(nums)):
            nums[i] = m[nums[i]]
            
        return nums
            
            
        
                