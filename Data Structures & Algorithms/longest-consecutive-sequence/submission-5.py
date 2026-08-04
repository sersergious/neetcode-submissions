class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time
        # Reflection
        
        longest = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                streak = 1
                while (num + streak) in numSet:
                    streak += 1
                longest = max(streak, longest)
            numSet.add(num)
          
        return longest
