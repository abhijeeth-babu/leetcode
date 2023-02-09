class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}

        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str not in word_map:
                word_map[sorted_str] = []
            word_map[sorted_str].append(word)
        
        res = []

        for value in word_map.values():
            res.append(value)
            
        return res
    
