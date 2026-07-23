class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hM = {}

        for i in range(len(nums)):
            numJ = target - nums[i]

            if numJ not in hM:
                hM[nums[i]] = i
                continue
            elif numJ + nums[i] == target and numJ in hM:
                return [min(i, hM[numJ]), max(i, hM[numJ])]
        
        return []

                