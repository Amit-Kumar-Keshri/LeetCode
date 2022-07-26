class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=[0]*26

        # for i in range(26):
        #     l1.append(0)

        for i in s:
            l1[ord(i)-97] += 1
            
        for i in t:
            l1[ord(i)-97] -= 1   
            
        if l1.count(0)==26:
             return 1
        return 0