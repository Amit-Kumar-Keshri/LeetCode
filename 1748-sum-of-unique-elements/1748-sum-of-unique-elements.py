class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        l = []
        for i in nums:
            if m[i] == 1:
                l.append(i)
        return sum(l)