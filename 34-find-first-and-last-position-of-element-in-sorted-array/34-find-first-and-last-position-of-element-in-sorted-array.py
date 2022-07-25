class Solution:
    def firstoccr(self, nums,target):
        first = -1
        l = 0
        h = len(nums)-1
        if len(nums)==0:
            return -1
        while l<=h:
            m = (l+h)//2
            temp = nums[m]
            if temp==target:
                first = m
                h = m-1
            elif target > temp:
                l = m+1
            else:
                h = m-1
        return first
    def lastoccr(self, nums,target):
        last = -1
        l = 0
        h = len(nums)-1
        if len(nums)==0:
            return -1
        while l<=h:
            m = (l+h)//2
            temp = nums[m]
            if temp==target:
                last = m
                l = m+1
            elif target > temp:
                l = m+1
            else:
                h = m-1
        
        return last
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstoccr(nums,target),self.lastoccr(nums,target)]
                    