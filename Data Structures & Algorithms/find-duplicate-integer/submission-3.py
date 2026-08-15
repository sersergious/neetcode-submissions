class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        slowClone = 0

        while slowClone != slow:
            slow = nums[slow]
            slowClone = nums[slowClone]

        return slow
