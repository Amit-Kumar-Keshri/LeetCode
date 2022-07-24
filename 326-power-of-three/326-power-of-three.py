class Solution:
    def rec(self,i,n):
        if i>n:
            return False
        if i == n:
            return True
        return self.rec(i*3,n)
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0 or n==2:
            return False
        if n==1:
            return True
        return self.rec(3,n)
            
        