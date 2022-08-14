class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        for i in range(2,num+1):
            #print(i)
            if i < 9 and i%2 == 0:
                c += 1
            elif i > 9:
                s = 0
                while i:
                    s += i%10
                    i //=10
                if s%2 == 0:
                    c += 1
        return c
                    