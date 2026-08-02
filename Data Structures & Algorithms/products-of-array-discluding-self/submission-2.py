class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix  multiplication
        prefix, suffix = [1]*len(nums), [1]*len(nums)
        i=1
        while i < len(nums):
            prefix[i] = prefix[i-1] * nums[i-1]
            i += 1
        
        i = len(nums) - 2

        while i >= 0:
            suffix[i] = suffix[i+1] * nums[i+1]
            i -= 1

        while i < len(nums):
            nums[i] = prefix[i] * suffix[i]
            i += 1
        
        return nums
