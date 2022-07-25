class Solution:
    def s(self,n):
        s = 0
        while n>0:
            t = n%10
            s += t**2
            n//=10
        return s
            
    def isHappy(self, n: int) -> bool:
        repeat = set()
        while True:
            repeat.add(n)
            n = self.s(n)
            if n==1:
                return True
            elif n in repeat:
                return False
            
            