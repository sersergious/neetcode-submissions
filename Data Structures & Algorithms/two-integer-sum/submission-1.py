class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashNums = {}

        for i in range(len(nums)):
            hashNums[nums[i]] = i 

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashNums.keys() and hashNums.get(diff) != i:
                result.append(hashNums.get(diff))
                result.append(i)
                break
            else: 
                continue

        return sorted(result)
        