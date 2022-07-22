class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        x = 9999999
        c = 0
        for i in strs:
            x = min(x,len(i))
        for i in range(x):
            y = 0
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    y =1
                c = j
            if y==1:
                break
            ans += strs[c][i]
        return ans