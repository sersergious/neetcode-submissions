class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time 
        # Reflection

        l, r = 1, max(piles) # O(n)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            
            total = 0
            for pile in piles:
                total += math.ceil(float(pile) / k)

            if total > h:
                l = k + 1
            else:
                res = k
                r = k - 1


        return res