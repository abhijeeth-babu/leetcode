class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = [0] * 128

        left = 0
        max_len = 0

        for right in range(len(s)):
            char_set[ord(s[right])] += 1
            while char_set[ord(s[right])] > 1:
                char_set[ord(s[left])] -= 1
                left += 1
            length = right - left + 1
            max_len = max(length, max_len)
        return max_len
