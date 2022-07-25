class Solution:
    def s(self,n):
        n = str(n)
        res = 0
        for i in n:
            res += int(i)**2
        return res
    def isHappy(self, n: int) -> bool:
        repeat = set()
        while True:
            repeat.add(n)
            n = self.s(n)
            if n==1:
                return True
            elif n in repeat:
                return False
            
            