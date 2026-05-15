class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst = [0]*26
        lst2 = [0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            lst[ord(s[i]) - ord('a')] += 1
            lst2[ord(t[i]) - ord('a')] += 1
        return lst == lst2