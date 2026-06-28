class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 0:
            return []

        numStr = ""

        for digit in digits:
            numStr += str(digit)

        num = int(numStr)   
        num += 1

        numStr = str(num)
        digits = []
        
        for digit in numStr:
            digits.append(int(digit))

        return digits

