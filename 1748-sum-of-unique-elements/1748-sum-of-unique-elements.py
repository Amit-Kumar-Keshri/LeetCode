class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        l = 0
        for i in nums:
            if m[i] == 1:
                l += i
        return l