class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = {}
        l2 = {}
        for i in range(len(s)):
            l1[ord(s[i]) - ord('a')] = 1 + l1.get(ord(s[i]) - ord('a'), 0)
            l2[ord(t[i]) - ord('a')] = 1 + l2.get(ord(t[i]) - ord('a'), 0)
        return l1==l2

        