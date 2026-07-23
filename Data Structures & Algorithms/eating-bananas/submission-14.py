class Solution:
    # Solution time: 43 minutes - 2nd time
    # Reflection: got 70% of the algo by myself with hints
    # the rest with the help of AI. I was stuck with the computing the k

    # Soluton time: 6:46 - 3rd time, fresh after the look up
    # I understand the algo, just confused as to why
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            k = l + (r - l) // 2
            time = 0
            
            for pile in piles:
                time += math.ceil(float(pile) / k)
            
            if time > h:
                l = k+1
            else:
                res = k
                r = k - 1
        
        return res
        
            