class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, cur, total):
            if i > len(nums)-1 or total > target:
                return 

            if total == target:
                res.append(cur.copy())
                return
            
            # Decision to include nums
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])

            # Decision to not include nums
            cur.pop()
            backtrack(i+1, cur, total)
        
        backtrack(0, [], 0)
        return res
