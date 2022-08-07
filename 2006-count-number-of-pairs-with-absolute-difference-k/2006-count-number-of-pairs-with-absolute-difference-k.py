class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = 0
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
                
        for i in nums:
            if i+k in m:
                c += m[i+k]
                
        return c