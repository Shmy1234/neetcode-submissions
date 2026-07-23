class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, m = 0, 0, 0
        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
            else:
                m = max(m, len(s[i:j]))
                i += 1
        return m
