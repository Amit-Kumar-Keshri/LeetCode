class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 0
        while i < n and j < n-1:
            if nums[i]==0 and nums[j+1]!=0:
                nums[i], nums[j+1] = nums[j+1], nums[i]
                i += 1
                j += 1
            elif nums[i]!= 0 and nums[j+1]==0:
                i+=1
            elif nums[i] == 0 and nums[j+1] == 0:
                j+=1
            else:
                i +=1
                j +=1
