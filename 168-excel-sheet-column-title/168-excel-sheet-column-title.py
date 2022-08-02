class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber != 0:
            columnNumber -=1
            x = columnNumber%26
            s = chr(x+65) +s
            columnNumber = columnNumber //26
        return s