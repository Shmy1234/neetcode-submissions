class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for char in s:
            if char.isalnum():
                s2 += char.lower() 
        for i in range(len(s2)//2):
            if s2[i] != s2[len(s2) - 1 - i]:
                return False
        
        return True


        