class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for i in s:
            if i == "(" or i=="{" or i== "[":
                ans.append(i)
            else:
                if i == ")":
                    if ans and ans[-1] == "(":
                        ans.pop()
                    else:
                        return 0
                elif i == "}":
                    if ans and ans[-1] == "{":
                        ans.pop()
                    else:
                        return 0
                elif i == "]":
                    if ans and ans[-1] == "[":
                        ans.pop()
                    else:
                        return 0
        if len(ans) == 0:
            return 1
        return 0