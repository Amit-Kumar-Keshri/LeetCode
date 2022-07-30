class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}
        
        c = 0
        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]] = t[i]
            elif s1[s[i]] != t[i]:
                return False
            
            if t[i] not in t1:
                t1[t[i]] = s[i]
            elif t1[t[i]] != s[i]:
                return False
        return True
            
                
            
