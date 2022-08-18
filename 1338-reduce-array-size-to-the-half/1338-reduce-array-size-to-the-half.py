class Solution:
    def minSetSize(self, nums: List[int]) -> int:
        dic = {}
        
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        N = len(nums)//2
        c = 0
        for i,j in dic.items():
            if N <= 0:
                return c
            N-=j
            c+=1
        return c