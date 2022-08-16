class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = set()
        
        for i,ch in enumerate(s):
            if ch not in m:
                m.add(ch)
                if s.count(ch)==1:
                    return i
        return -1
    
                
                
            