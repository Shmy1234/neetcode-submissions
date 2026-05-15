class Solution:
    def validPalindrome(self, s: str) -> bool:
        for c in s:
            s2 = s.replace(c, "")
            if s2 == s2[::-1]: 
                return True 
        return False