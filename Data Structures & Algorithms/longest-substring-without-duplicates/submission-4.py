class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i, j = 0, 1
        while j <= len(s) - 1:
            if s[j] not in s[i:j]:
                j += 1
            else:
                max_len = max(max_len, len(s[i:j]))
                i += 1

        return max(max_len, len(s[i:j]))