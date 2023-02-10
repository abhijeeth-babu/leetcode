class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        char_map = [0] * 26
        for char in s1:
            char_map[ord(char) - ord('a')] += 1
        left, size, count = 0, len(s1), len(s1)

        for right in range(len(s2)):
            right_index = ord(s2[right]) - ord('a')
            if char_map[right_index] > 0:
                count -= 1
            char_map[right_index] -= 1
            while count == 0:
                if right - left + 1 == size:
                    return True
                left_index = ord(s2[left]) - ord('a')
                if char_map[left_index] >= 0:
                    count += 1
                char_map[left_index] += 1
                left += 1
        return False
