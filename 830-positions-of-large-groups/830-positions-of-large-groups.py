class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l = 0
        r = 0
        ans = []
        for i in range(len(s)):
            if i == len(s)-1 or s[l] != s[r+1]:
                if r-l+1 >= 3:
                    ans.append([l,r])
                l = i+1
            r +=1
        return ans
            
            
                