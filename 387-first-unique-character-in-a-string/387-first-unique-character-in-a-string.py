class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = [0]*26
        
        for i,ch in enumerate(s):
            m[ord(ch)-97] += 1
                
        for i,ch in enumerate(s):
            if m[ord(ch)-97] == 1:
                return i
        return -1
    
                
                
            