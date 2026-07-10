class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0

        for r in range(len(prices)):
            earn = prices[r] - prices[l]
            profit = max(profit, earn)

            while prices[r] < prices[l]:
                l += 1
        
        return profit

            