class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        
        for i in s:
            if i.islower():
                strs+=i
            elif i.isupper():
                strs+=i.lower()
            elif i.isnumeric():
                strs+=i
            # else:
            #     continue
        print(strs)
        l = 0
        h = len(strs)-1
        while l<=h:
            if strs[l]!=strs[h]:
                return False
            else:
                l += 1
                h -= 1
            
        return True
            