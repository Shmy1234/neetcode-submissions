class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k=3, ABCCAABBCC
        i = 0
        j = 0
        d={}
        n = 0
        m = 0
        while j < len(s):
            d[s[j]] = 1 + d.get(s[j], 0)
            n = max(n, d[s[j]])
            while j-i+1 - n > k:
                d[s[i]] -= 1
                i+=1
            m = max(m, j-i+1)
            j+=1
        return m

        