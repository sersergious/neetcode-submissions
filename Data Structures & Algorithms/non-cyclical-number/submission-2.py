class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            totalSum = 0

            while n > 0:
                totalSum += (n % 10) ** 2
                n //= 10 

            n = totalSum
        
        return n == 1