class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l = 0
        u = 0
        for i in moves:
            if i == "R":
                l += 1
            elif i == "L":
                l -= 1
            elif i == "U":
                u += 1
            else:
                u -= 1
        if l == 0 and u == 0:
            return True
        return False