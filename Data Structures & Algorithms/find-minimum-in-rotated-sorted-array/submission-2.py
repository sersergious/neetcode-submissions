class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Time
        #Reflection

        l, h = 0, len(nums) - 1
        minSoFar = nums[l]
        while l <= h:
            mid = (l + h) // 2
            minSoFar = min(minSoFar, nums[mid])

            if nums[h] < nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        
        return minSoFar
