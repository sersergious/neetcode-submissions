class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if(len(nums) == 0):
            return []

        n = len(nums)
        prefix = {0: 1}
        suffix = {n-1: 1}
        output = []

        i = 1
        while i < n:
            prefix[i] = nums[i-1] * prefix[i-1]
            i += 1

        i = n-2
        while i >= 0:
            suffix[i] = nums[i+1] * suffix[i+1]
            i -= 1
            

        print(prefix)
        print(suffix)

        i = 0
        while i < n:
            product = prefix[i] * suffix[i]
            print(product)
            output.append(product)
            i += 1

        return output