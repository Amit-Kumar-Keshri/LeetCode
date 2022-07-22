class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        s = 0
        while temp>0:
            s = (s * 10) + (temp%10)
            temp //= 10
        if x == s:
            return 1
        return 0
            