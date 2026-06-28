class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        
        result = min(heights[right], heights[left]) * (right - left)
       
        left = 1 
        
        while left <= right:
            amount = min(heights[right], heights[left]) * (right - left) 

            if amount > result:
                result = amount
            
            if min(heights[right], heights[left]) == heights[right]:
                right -= 1
            else:
                left += 1
        
        return result