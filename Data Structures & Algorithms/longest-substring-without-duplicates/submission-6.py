class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, m = 0, 0, 0 
        while j < len(s):
            if i != j and s[j] in s[i:j]:
                m = max(m, len(s[i:j]))
                i = j 
                j+=1
            else:
                j+=1 
        
        return m
