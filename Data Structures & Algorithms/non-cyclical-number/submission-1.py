class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            seen.add(n)
            digits = str(n)
            sum = 0 

            for digit in digits:
                num = int(digit)
                sum += num ** 2

            if sum in seen:
                return False
            
            n = sum

        return True