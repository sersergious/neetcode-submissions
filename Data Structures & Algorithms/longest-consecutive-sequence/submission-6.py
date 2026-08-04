class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: 25 minutes
        # Reflection: i was trying to build a seen set and the algorithm was basically if num - 1 the seen then extend the streak, otherwise reset to 0. However, it only if the consecutive streak is dispersed ascending order across the array. Instead, I should have   
        
        longest = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                streak = 1
                while (num + streak) in numSet:
                    streak += 1
                longest = max(streak, longest)
          
        return longest
