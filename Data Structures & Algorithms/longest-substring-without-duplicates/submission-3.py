class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, l = 0, 0, 0
        c = ''
        while j < len(s):
            if s[j] in c:
                l = max(l, len(c))
                c=''
                i+=1
            else:
                c+=s[j]
                j+=1
            
        return max(l, len(c))