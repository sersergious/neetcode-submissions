class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)

            # decision not to inlcude nums[i]
            subset.pop()
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res