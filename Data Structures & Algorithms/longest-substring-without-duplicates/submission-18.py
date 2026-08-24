class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        i = 0
        m = 0
        for j in range(len(s)):
            while s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            hashset.add(s[j])
            m = max(m, j - i + 1)
            j+=1
        return m
