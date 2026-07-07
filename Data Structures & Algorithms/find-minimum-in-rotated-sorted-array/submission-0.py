class Solution:
    def findMin(self, nums: List[int]) -> int:
        minSoFar = nums[0] 

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < minSoFar:
                minSoFar = nums[mid]
                r = mid - 1
            else:   
                l = mid + 1

        return minSoFar