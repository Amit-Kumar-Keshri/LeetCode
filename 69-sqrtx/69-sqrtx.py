class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return x
        
        l = 0
        h = x//2
        while l<=h:
            m = (l+h)//2
            s = m*m
            
            if s == x:
                return m
            elif s > x:
                h = m-1
            else:
                l = m+1
        return h