#from copy import deepcopy
class Solution:
    # possible permutations
    def fact(self, n: int) -> int:
        if n==0:
            return 1
        return n*self.fact(n-1)
    # finding next permutation
    def nxtper(self, nums):

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
        x = self.fact(n)
        ans = []
        
        i = 0
        while i < x: 
            a= self.nxtper(nums)
            ans.append(a[:])
            i+= 1
            
        return ans