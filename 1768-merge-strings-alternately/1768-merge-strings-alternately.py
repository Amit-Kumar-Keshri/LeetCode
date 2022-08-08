class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        
        l = 0
        r = 0
        
        while l<len(word1) and r<len(word2):
            s += word1[l] + word2[r]
            l += 1
            r += 1
        
        while l<len(word1):
            s += word1[l]
            l += 1
            
        while r<len(word2):
            s += word2[r]
            r += 1
        
        return s