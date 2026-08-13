class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0

        for r in range(len(prices)):
            earn = prices[r] - prices[l]
            profit = max(profit, earn)

            while l < r and prices[r] - prices[l] < 0:
                l += 1
            
        return profit