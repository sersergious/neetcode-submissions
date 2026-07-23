class Solution:
    # Add 5 minutes 
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        # Two ptrs
        # left += 1 when < right

        l, r = 0, len(heights) - 1
        maxVol = 0

        while l < r:
            vol = max((r - l), (l-r)) * min(heights[l], heights[r])

            maxVol = max(maxVol, vol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxVol