class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs[0])
        for s in strs: 
            m = min(m, len(s)) 
        
        p = ""
        for i in range(m):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return p
            p += c
        return p
