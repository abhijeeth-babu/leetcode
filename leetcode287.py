class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                new_slow = 0
                while True:
                    slow = nums[slow]
                    new_slow = nums[new_slow]
                    if new_slow == slow:
                        return slow
