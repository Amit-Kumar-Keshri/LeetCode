class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
                
        for i,j in enumerate(s):
            if j in m and m[j] == 1:
                return i
        return -1