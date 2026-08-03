class Solution:
    def binarySearch(self, nums, target, l, h):
        
        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return -1 

    def search(self, nums: List[int], target: int) -> int:
        # Time:
        # Reflection:

        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid - 1

        if nums[len(nums) - 1] < target:
            return self.binarySearch(nums, target, 0, l-1)
        else:
            return self.binarySearch(nums, target, l, len(nums) - 1)        
         