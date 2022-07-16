class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 9999999
        max_profit = 0
        for i in prices:
            if i - min_price > max_profit:
                max_profit = i - min_price
            if i < min_price:
                min_price = i
        return max_profit