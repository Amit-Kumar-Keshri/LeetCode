class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        if nums[l] <= nums[h]:
            return nums[l]
        while l <= h:
            m = (l+h)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m] > nums[l]:
                l = m+1
            else:
                h = m-1