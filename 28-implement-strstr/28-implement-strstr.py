class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        if len(haystack)<len(needle):
            return -1
        f = 0
        while f < len(haystack):
            if needle[0] == haystack[f]:
                nee = 0
                fee= f
                while nee < len(needle) and fee < len(haystack):
                    if needle[nee] != haystack[fee]:
                        break
                    nee+=1
                    fee+=1
                if nee == len(needle):
                    return f  
            f+=1
        return -1
                 
                
        
        