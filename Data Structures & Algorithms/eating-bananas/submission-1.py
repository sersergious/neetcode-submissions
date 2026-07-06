class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minK = piles[0]
        
        #Brute force
        # for bananas in piles:
        #     time = 0
            
        #     for i in range(len(piles)):
        #         if piles[i] <= bananas: # if there's < k bananas in the pile
        #             time += 1
        #         else: # if the there's more than k bananas in the pile
        #             time += piles[i] / bananas 
            
        #     minK = bananas if time <= h else minK
        
        low, high = 1, max(piles) # o(n)
        res = high 

        while low <= high:
            k = low + (high - low) // 2
            time = 0

            for p in piles:
                time += math.ceil(float(p) / k)

            if time <= h:
                res = k
                high = k - 1
            else:
                low = k + 1

        return res