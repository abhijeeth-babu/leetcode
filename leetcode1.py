class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_map = {}
        for i, num in enumerate(nums):
            if target - num in data_map:
                return [data_map[target - num], i]
            data_map[num] = i
