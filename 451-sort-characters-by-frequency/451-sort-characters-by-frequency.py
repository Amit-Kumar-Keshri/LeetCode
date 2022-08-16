class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}
        
        for ch in s:
            if ch not in m:
                m[ch] = 1
            else:
                m[ch] += 1
        
        dict_item = dict(sorted(m.items(), key=lambda value:value[1], reverse = True))
        # print(dict_item)
        ans = ""
        for i in dict_item:
            ans += i*dict_item[i]
            
        return ans
            