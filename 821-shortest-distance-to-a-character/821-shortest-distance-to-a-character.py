class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        index_c = []
        res = []
        for i in range(len(s)):
            if s[i] == c:
                index_c.append(i)
        l = 0
        r= 0
        for i in range(len(s)):
            if i >index_c[r]:
                l = r
                if r<len(index_c)-1:
                    r+=1
            res.append(min(abs(i-index_c[l]),abs(i-index_c[r])))
        return res
            
                