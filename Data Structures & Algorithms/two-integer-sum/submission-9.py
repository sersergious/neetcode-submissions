class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hM = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff not in hM:
                hM[nums[i]] = i
                continue 
            
            if diff + nums[i] == target:
                return [min(i, hM[diff]), max(i, hM[diff])]
             

            


