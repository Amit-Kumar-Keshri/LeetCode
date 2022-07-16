class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low<=high):
            i = (high+low)//2
            m = nums[i]
            if target == m:
                return i
            if target > m:
                low = i+1
            else:
                high = i-1
        return -1