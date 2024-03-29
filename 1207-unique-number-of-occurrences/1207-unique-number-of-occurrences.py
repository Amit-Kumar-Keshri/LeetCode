class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        
        for i in arr:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        
        x = set()
        for i in m.values():
            if i in x:
                return False
            else:
                x.add(i)
        return True