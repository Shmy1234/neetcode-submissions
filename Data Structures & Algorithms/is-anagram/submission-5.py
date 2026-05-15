class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d_s = {}
        d_t = {}
        for i in range(len(s)):
            d_s[ord(s[i])] = 1 + d_s.get(ord(s[i]), 0)
            d_t[ord(t[i])] = 1 + d_t.get(ord(t[i]), 0)
        return d_s == d_t