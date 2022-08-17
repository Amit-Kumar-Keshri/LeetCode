class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        l, dup, mis = len(nums), 0, 0
        for num in nums:
            if nums[abs(num) - 1] < 0 :
                dup = abs(num)
            else: nums[abs(num) - 1] *= -1
        
        for index in range(l):
            if nums[index] > 0:
                mis = index + 1
                break
                
        return [dup, mis]