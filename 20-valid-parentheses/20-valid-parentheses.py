class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {"(":")","{":"}","[":"]"}
        for el in s:
            if el in m:
                st.append(el)
            else:
                if len(st)==0:
                    return 0
                elif m[st[-1]] == el:
                    st.pop()
                else:
                    return 0
        if len(st)==0:
            return 1
        else:
            return 0
        
        