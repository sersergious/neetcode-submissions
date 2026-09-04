class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtrack(cur, total, i):
            if total == target:
                combinations.append(cur.copy())
                return
            
            if i > len(candidates) - 1 or total > target:
                return
            
            cur.append(candidates[i])
            backtrack(cur, total + candidates[i], i+1)

            cur.pop()

            # optimization trick i look up in the solution to skip over similar elements
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(cur, total, i+1)

        backtrack([], 0, 0)
        return combinations

        