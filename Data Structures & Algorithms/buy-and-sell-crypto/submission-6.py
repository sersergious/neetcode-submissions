class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Second attempt - 36 mins

        profit = 0
        
        l = 0
        for r in range(len(prices)):

            profit = max(profit, prices[r]- prices[l])

            while prices[r]- prices[l] < 0:
                l += 1
        
        return profit
        