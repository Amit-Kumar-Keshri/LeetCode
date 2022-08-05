class Solution:
    def groupAnagrams(self, nums: List[str]) -> List[List[str]]:
        m = {}
        
        n = len(nums)
        for i in nums:
            x = sorted(i)
            y = "".join(x)
            
            if y not in m:
                m[y] = [i]
                
            else:
                 m[y].append(i)
                
        return m.values()