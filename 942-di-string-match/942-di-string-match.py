class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        l = 0
        h= len(s)
        for i in s:
            if i == "I":
                ans.append(l)
                l += 1
            else:
                ans.append(h)
                h -= 1
        s1 = 0
        for i in range(1,len(s)+1):
            s1 += i
        ans.append(s1 - sum(ans))
        return ans   