class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        m ={}
        
        for i in stones:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        print(m)     
        c = 0
        for i in jewels:
            if i in m.keys():
                c += m[i]
        
        return c