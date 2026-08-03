class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hM = {}

        for i in range(len(nums)):
            if target - nums[i] not in hM:
                hM[nums[i]] = i   
                continue
            
            num = target - nums[i]

            if num + nums[i] == target:
                return [min(i, hM[num]), max(i, hM[num])]

        return []
                