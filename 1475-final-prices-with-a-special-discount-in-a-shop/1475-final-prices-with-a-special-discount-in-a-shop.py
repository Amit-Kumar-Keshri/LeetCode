class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        l = []
        for i in reversed(prices):
            while st and i<st[-1]:
                st.pop()
            
            if len(st)==0:
                l.append(i)
            else:
                l.append(i-st[-1]) 
            st.append(i)
        
        return l[::-1]
#         for i in range(len(prices)):
#             if prices[i] in m.keys():
#                 prices[i] = m[prices[i]]
#         return prices
                
                