from copy import deepcopy
class Solution:
    def fact(self, n: int) -> int:
        if n==0:
            return 1
        return n*self.fact(n-1)
    
    def nxtper(slef, nums):

        i = j = len(nums)-1
        while i > 0 and nums[i-1] > nums[i]:
            i -=1


        while j > 0 and nums[i-1] > nums[j]:
            j-=1
        nums[i-1], nums[j] = nums[j], nums[i-1]

        left = i
        right = len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # x = 1
        # for i in range(1,n+1):
        #     x *= i
        x = self.fact(n)
        ans = []
        
        i = 0
        while i < x: 
            self.nxtper(nums)
            ans.append(deepcopy(nums))
            i+= 1
            
        return ans