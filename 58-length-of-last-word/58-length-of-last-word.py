class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l1 = s.strip()
        l = list(l1.split(" "))
        
        print(l)
        
        return (len(l[-1]))