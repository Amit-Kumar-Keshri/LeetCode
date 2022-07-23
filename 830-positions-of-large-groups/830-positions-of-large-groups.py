class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l = 0
        ans = []
        for i in range(len(s)):
            if i == len(s)-1 or s[l] != s[i+1]:
                if i-l+1 >= 3:
                    ans.append([l,i])
                l = i+1
        return ans
            
            
                