class Solution:
    def s(self,n):
        n = str(n)
        res = 0
        for i in n:
            res += int(i)**2
        return res
    def isHappy(self, n: int) -> bool:
        t=n
        c = 0
        while t>0:
            c+=1
            t//=10
        if c==1:
            c = n
        else:
            c = c**2+1
        while c>0:
            n=self.s(n)
            if n==1:
                return True
            c-=1
        return False