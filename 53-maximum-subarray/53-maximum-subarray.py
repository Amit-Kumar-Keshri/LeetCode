class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr= 0
        max_sum = -99999
        
        for i in nums:
            curr += i
            if curr > max_sum:
                max_sum = curr
            if curr < 0:
                curr = 0
        return max_sum