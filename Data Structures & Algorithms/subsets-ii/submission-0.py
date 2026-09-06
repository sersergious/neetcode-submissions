class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, cur):
            if len(nums) <= i:
                if cur not in res:
                    res.append(cur.copy())
                return
            
            # decision to append
            cur.append(nums[i])
            backtrack(i+1, cur)

            # decision not to append
            cur.pop()
            backtrack(i+1, cur)
        
        backtrack(0, [])
        return res
