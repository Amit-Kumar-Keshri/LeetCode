class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return int(Counter(s)==Counter(t))