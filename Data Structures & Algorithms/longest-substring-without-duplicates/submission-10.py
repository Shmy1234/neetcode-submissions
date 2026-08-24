class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        s2 = s[0]
        m = 0
        while j < len(s):
            if s[j] not in s2:
                s2 += s[j]
                j+=1
                m = max(m, len(s2))
            else:
                i+=1
                s2 = s2[1:]
        
        return m
            