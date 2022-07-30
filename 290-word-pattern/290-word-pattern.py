class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li = list(s.split(" "))
        
        p1 ={}
        s1 = {}
        if len(li) != len(pattern):
            return False
        for i in range(len(li)):
            if li[i] not in p1:
                p1[li[i]] = pattern[i]
            elif p1[li[i]] != pattern[i]:
                return False
            
            if pattern[i] not in s1:
                s1[pattern[i]] = li[i]
            elif s1[pattern[i]] != li[i]:
                return False
        
        return True