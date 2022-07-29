class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            if nums[l] == val:
                nums[l] = nums[r]
                nums.pop()
                r -= 1
            else:
                l += 1