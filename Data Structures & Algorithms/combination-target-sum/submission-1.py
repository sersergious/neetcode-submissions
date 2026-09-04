# Time: 49
# Reflection: my initial approach was based off of the prev Subset problem where i make the decisions based for the base case on completely different idea. Core flaw was i though i can continuusly scan thru all the posibilities, which is why i though i=0 is cool and i+1 was excluding duplicates. For now just gotta understand that we actually exclude numbers only if we know 

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
