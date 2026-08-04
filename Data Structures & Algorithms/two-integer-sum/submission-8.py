class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hM = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hM and diff + nums[i] == target:
                return [min(i, hM[diff]), max(i, hM[diff])]

            hM[nums[i]] = i
        
        return []