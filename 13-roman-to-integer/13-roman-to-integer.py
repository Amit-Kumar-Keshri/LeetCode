class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # Translates the Roman numbers
        
        res = 0
        
        for i, c in enumerate(s[:-1]):  # use s[:1] so there's no need to check index
            if nums[c] < nums[s[i + 1]]: res -= nums[c] 
            #if the number < the next number, subtract the number
            
            else: res += nums[c]    # else add the number  
                
        return res + nums[s[-1]]