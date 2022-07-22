class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        ans = ''
        m1, m2 = max(strs), min(strs)
        for i, ch in enumerate(m2):
            if m1[i] != ch:
                break
            else:
                ans += ch
        return ans