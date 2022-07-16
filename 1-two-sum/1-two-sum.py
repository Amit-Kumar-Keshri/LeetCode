class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,el in enumerate(nums):
            if target - el in result:
                return (result[target - el],i)
            result[el] = i