class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        curr_min = prices[0]
        for price in prices:
            curr_min = min(price, curr_min)
            profit = price - curr_min
            max_profit = max(profit, max_profit)
        
        return max_profit
