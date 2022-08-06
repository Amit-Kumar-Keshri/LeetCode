class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        m = {}
        # print(x)
        c = 0
        for i in key:
            if i!=" " and i not in m:
                m[i] = chr(97+c)
                c+=1
        s= ""
        for i in message:
            if i!=" ":
                s += m[i]
            else:
                s+=" "
        return s