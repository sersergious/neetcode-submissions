class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        
        def backtrack(i, total):
            if target == total:
                res.append(cur.copy())
                return


            if i >=len(nums) or total > target:
                return
            
            cur.append(nums[i])
            backtrack(i, total + nums[i])
            cur.pop()
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res