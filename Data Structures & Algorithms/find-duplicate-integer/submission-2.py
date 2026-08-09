class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if fast == slow:
                break

        slowEntry = 0

        while True:
            slow = nums[slow]
            slowEntry = nums[slowEntry]

            if slow == slowEntry:
                return slow

        
