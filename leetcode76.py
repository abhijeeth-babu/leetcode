class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        min_len = m + 1
        char_map = [0] * 128
        for char in t:
            char_map[ord(char)] += 1
        left, counter = 0, n
        start = 0
        for right in range(m):
            right_index = ord(s[right])
            if char_map[right_index] > 0:
                counter -= 1
            char_map[right_index] -= 1
            while counter == 0:
                if right - left + 1 <= min_len:
                    start = left
                    min_len = right - left + 1
                left_index = ord(s[left])
                if char_map[left_index] >= 0:
                    counter += 1
                char_map[left_index] += 1
                left += 1
        if min_len == m + 1:
            return ""
        return s[start:start + min_len]
