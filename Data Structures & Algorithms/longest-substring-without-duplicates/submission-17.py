class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # len substring (j - i + 1)
        # s[j] in substring
        hashset = set()
        m = 0
        i = 0
        for j in range(len(s)):
            while s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            hashset.add(s[j])
            m = max(m, j - i + 1)
        
        return m
