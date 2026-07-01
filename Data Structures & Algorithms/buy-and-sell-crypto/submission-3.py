class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit thus far = prices[right] - prices[left]
        # if total < maxProfit
        #       update total 
        #      left += 1
        # LEFT POINTER INCREASE WHEN PROFIT ON ITH DAY < TOTAL PROFIT
        # OTHE WISE UPDATE WITH THE MAX RIGHT++
        # IF NEG PROFIT RETURN 0

        profit = 0
        
        l = 0
        for r in range(len(prices)):

            profit = max(profit, prices[r]- prices[l])

            while prices[r]- prices[l] < 0:
                l += 1
        
        return profit
        