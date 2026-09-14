# Time: 13
# Reflection: Third attempt - I struggled with coming with the shape of the code for some reason. This is a definitive regression from the previous becuase i was able to produce code cold previoulsy. This time I need to look up the solution to have the shape put together. 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue 
                
                used[i] = True
                cur.append(nums[i])
                backtrack(cur)
                cur.pop()
                used[i] = False
        
        backtrack([])
        return res

            
            

