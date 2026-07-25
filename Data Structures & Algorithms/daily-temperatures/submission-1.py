class Solution:
    # I debugged, but gave up, so i had to look at the Solution
    # Very Bad!
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                t, p = stack.pop()
                res[p] = i - p

            stack.append([temperatures[i], i])
            
        return res