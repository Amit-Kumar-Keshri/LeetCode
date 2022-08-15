class Solution:
    def addDigits(self, num: int) -> int:
        a = 0
        while num > 0:
            a += num % 10
            num //=10
            
            if num == 0 and a > 9:
                num = a
                a = 0
        return a
            
             