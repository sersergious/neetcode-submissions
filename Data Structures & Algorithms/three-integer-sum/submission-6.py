class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = 0
    
        
        while current < len(nums)-2:
            
            if current > 0 and nums[current] == nums[current - 1]:
                current += 1
                continue

            low = current +1
            high = len(nums) - 1
            
            while low < high: 
                
                if (nums[low] + nums[high] > -nums[current]):
                    high -= 1
                elif (nums[low] + nums[high] < - nums[current]):
                    low += 1
                else:
                    res.append([nums[low], nums[high], nums[current]])
                    low += 1
                    high -= 1
                    
                    while low < high and nums[low-1] == nums[low]:
                        low += 1
                    while low < high and nums[high+1] == nums[high]:
                        high -= 1
            
            current += 1
        
        

        return(res)
