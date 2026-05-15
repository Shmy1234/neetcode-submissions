class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        d2 = {}
        for i in range(len(s)):
            d[s[i]] = 1 + d.get(s[i], 0)
            d2[t[i]] = 1 + d2.get(t[i], 0)
        return d == d2