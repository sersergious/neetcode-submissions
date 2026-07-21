class Solution:
    # Solved in 
    # This is a redo - warm up
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0

        for r in range(len(prices)):
            earn = prices[r] - prices[l]
            profit = max(profit, earn)

            while prices[l] > prices[r]:
                l += 1
        
        return profit