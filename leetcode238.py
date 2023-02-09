class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        left_product = 1
        right_product = 1
        nums_len = len(nums)
        for i in range(nums_len):
            left_product = 1 if i == 0 else left_product * nums[i - 1]
            res[i] *= left_product
            right_product = 1 if i == 0 else right_product * nums[nums_len - i]
            res[nums_len - i - 1] *= right_product
            
        return res
