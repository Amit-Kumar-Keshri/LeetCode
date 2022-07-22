class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        st = []
        for i in s:
            if i=="(":
                if len(st):
                    ans.append(i)
                st.append(i)
            else:
                st.pop()
                if len(st)!= 0:
                    ans.append(i)
        return "".join(ans)
                