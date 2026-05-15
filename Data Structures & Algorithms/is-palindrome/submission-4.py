class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for i in range(len(s)):
            if s[i].isalnum():
                s2 += s[i].lower()

        for i in range(len(s2)//2):
            if s2[i] != s2[len(s2) - 1 - i]:
                return False
        
        return True
        