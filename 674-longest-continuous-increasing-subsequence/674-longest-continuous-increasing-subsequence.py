class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        r = 0
        curr = 0
        maxi = 0
        n = len(nums)
        if n==1:
            return 1
        while r != n:
            
            if (nums[r-1] >= nums[r]):
                maxi = max(curr, maxi)
                curr = 0
            elif r == n-1:
                maxi = max(curr+1, maxi)
                
            curr += 1
            r += 1
                
        # l = nums[l:r+1]          
        return maxi