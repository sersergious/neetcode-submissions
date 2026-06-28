class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = 0

        for sell in range(1, len(prices)):
            earn = prices[sell] - prices[buy]
            
            if earn > profit:
                profit = earn
            elif earn < 0:
                while buy < sell and (prices[sell] - prices[buy]) < 0:
                    buy += 1
            else:
                continue 

        return profit