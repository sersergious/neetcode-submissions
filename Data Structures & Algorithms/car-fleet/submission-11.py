class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time x + 2 minutes
        # Reflection 

        cars = list(zip(position, speed))
        cars.sort(reverse=True) 
        stack = []

        for p, s in cars:
            time = (target  - p) / s
            stack.append(time)
            
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            

        return len(stack)