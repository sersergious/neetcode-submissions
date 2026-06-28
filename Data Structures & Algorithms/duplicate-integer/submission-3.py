class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_occ = {}

        # this is to populate the dictionary
        for i in range(len(nums)):
            if nums[i] not in nums_occ.keys():
                nums_occ[nums[i]] = 1
            else: 
                nums_occ[nums[i]] += 1
        
        vals = list(nums_occ.values())

        # Now we need to check for the numbers
        for i in range(len(vals)): 
            if vals[i] > 1:
                return True
        
        return False
        
