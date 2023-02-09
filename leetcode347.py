class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1

        top_k_list = [[]] * (len(nums) + 1)
        for key, value in freq_dict.items():
            if not top_k_list[value]:
                top_k_list[value] = [key]
            else:
                top_k_list[value].append(key)

        res = []
        i = len(nums)
        while i >= 0 and len(res) < k:
            if top_k_list[i]:
                for val in top_k_list[i]:
                    res.append(val)
            i -= 1
        
        return res
