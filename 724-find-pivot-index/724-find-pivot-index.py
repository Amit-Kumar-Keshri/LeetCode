class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t_sum = 0
        c_sum = 0
        for i in nums:
            t_sum += i
            
        for j in range(len(nums)):
            t_sum -= nums[j]
            if c_sum == t_sum:
                return j
            else:
                c_sum += nums[j]
        return -1
            