class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k=3, ABCCAABBCC
        i = 0
        j = 0
        d={}
        n = 1
        m = 0
        while j < len(s):
            d[s[j]] = 1 + d.get(s[j], 0)
            while j-i+1 - n > k:
                i+=1
            n = max(n, d[s[j]])
            m = max(m, j-i+1)
            j+=1
        return m

        