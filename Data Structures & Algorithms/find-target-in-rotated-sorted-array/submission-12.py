class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minSoFar = nums[0]
        minIndex = 0
        l, r = 0, len(nums) - 1
        
        # This is to find the min
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < minSoFar:
                minSoFar = nums[mid]
                minIndex = mid
                r = mid - 1
            else:
                l = mid + 1

        if(minSoFar == target):
            return minIndex
        elif minIndex == 0:
            l, r = 0, len(nums) - 1
            
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        elif nums[minIndex -1] >= target and nums[0] <= target:
            l, r = 0, minIndex
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            l, r = minIndex + 1, len(nums) - 1
               
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1