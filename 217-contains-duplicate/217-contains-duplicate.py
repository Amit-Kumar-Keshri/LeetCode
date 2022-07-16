class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = len(set(nums))
        if res == len(nums):
            return 0
        else:
            return 1