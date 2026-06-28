
class Solution:
    def trap(self, height: List[int]) -> int:
        areaTotal = 0
        areaList = []

        left, right = 0, 1

        while right < len(height):
            next = height[right]
            
            if next < height[left]:
                areaList.append(height[left] - height[right])

            if next >= height[left]:
                while len(areaList) != 0:
                    areaTotal += areaList.pop()
                
                left = right

            right += 1 

        left, right = len(height) - 2, len(height) - 1
        areaList.clear()

        while left >= 0:
            next = height[left]
            
            

            if next < height[right]:
                areaList.append(height[right] - height[left])

            if next > height[right]:
                while len(areaList) != 0:
                    areaTotal += areaList.pop()
                
                right = left

            left -= 1 

        return areaTotal