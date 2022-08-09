class Solution:
    def firstUniqChar(self, s: str) -> int:
#         m = set()
#         ans = -1
#         i = 
#         for i in range(len(s)-1,-1,-1):
#             if s[i] not in m:
#                 m.add(s[i])
#                 ans = i
        
#         return ans
        for i in range(len(s)):
            # if s[i] not in visited:
            #     visited.add(s[i])
            if s.count(s[i]) == 1:
                return i
        return -1
                
            