class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')      # 正无穷（很大）
        max_profit = 0

        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(max_profit, p-min_price)
        
        return max_profit