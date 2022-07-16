class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return 0
        while(n!=0):
            if n==1:
                return 1
            elif n%2!=0:
                return 0
            else:
                n=n//2
        return 1