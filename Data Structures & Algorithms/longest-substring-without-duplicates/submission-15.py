class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        m=0
        i = 0
        for j in range(len(s)):
            while s[i] in s_set:
                s_set.remove(s[i])
                i+=1 
            s_set.add(s[j])
            m = max(m, j - i)
        return m
            