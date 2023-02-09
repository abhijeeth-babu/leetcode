class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data = [0] * 26
        for letter in s:
            data[ord(letter) - ord('a')] += 1
        for letter in t:
            data[ord(letter) - ord('a')] -= 1
        for num in data:
            if num:
                return False
        return True
