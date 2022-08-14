class Solution:
    def a_v(self, i):
        return ord(i)-96
    def getLucky(self, s: str, k: int) -> int:
        ans = ""
        for i in s:
            a = str(self.a_v(i))
            ans += a
        res = int(ans)   
        for i in range(k):
            a = 0
            while res:
                a += res%10
                res //=10
            res = a
        
        return res
            