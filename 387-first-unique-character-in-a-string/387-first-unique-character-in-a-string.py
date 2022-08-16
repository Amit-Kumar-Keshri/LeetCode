class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        
        for i,ch in enumerate(s):
            if ch not in m:
                m[ch] = 1
            else:
                m[ch] += 1
            
        print(m)
        for i,ch in enumerate(s):
            if m[ch] == 1:
                return i
        return -1
                
                
            