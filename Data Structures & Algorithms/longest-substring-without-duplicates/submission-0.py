class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i, j = 0, 1
        while i <= j <= len(s) - 1:
            print(s[i], i, s[j], j, max_len)
            if s[j] not in s[i:j]:
                j += 1
            else:
                max_len = max(max_len, len(s[i:j]))
                i += 1
        max_len = max(max_len, len(s[i:j]))
        print(max_len)
        return max_len


        