class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        i = 0
        j = 1
        s2 = s[0]
        m = 1
        while j < len(s):
            if s[j] not in s2:
                s2 += s[j]
                j+=1
                m = max(m, len(s2))
            else:
                i+=1
                s2 = s2[1:]
        
        return m
            