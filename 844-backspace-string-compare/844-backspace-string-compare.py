class Solution:
    def backspace(self,s):
        st = []
        for i in s:
            if i == "#" and len(st)!= 0:
                st.pop()
            elif len(st)==0 and i =="#":
                continue
            else:
                st.append(i)
        return "".join(st)
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.backspace(s)
        s2 = self.backspace(t)
        return True if s1==s2 else False
    