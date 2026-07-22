class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range((len(nums))):
            if i > 0 and nums[i] == nums[i-1]:  # Skip duplicate num1
                continue

            num1 = nums[i]
            l, r = i+1, len(nums) - 1

            while l < r:
                if  nums[l] + nums[r] == -num1:
                    res.append([num1, nums[r], nums[l]])

                    l += 1
                    r -= 1

                    while nums[l-1] == nums[l] and l < r:
                        l += 1

                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                    
                    

                elif nums[l] + nums[r] < -num1:
                    l += 1
                else:
                    r -= 1
            

        return res     