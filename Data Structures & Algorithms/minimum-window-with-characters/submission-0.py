class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, len(t)
        res, resLen = [-1, -1], float("infinity")
        dt, w = {}, {}
        for char in t:
            dt[char] = 1 + dt.get(char, 0)
        l, r = 0, 0
        while r < len(s):
            w[s[r]] = 1 + w.get(s[r], 0)
            if s[r] in dt and w[s[r]] == dt[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - 1 + 1
                
                w[s[l]] -= 1
                if s[l] in dt and w[s[l]] < dt[s[l]]:
                    have -= 1
                l += 1
            
            r += 1
        
        if resLen != float("infinity"):
            return s[res[0]: res[1] + 1]
        return ''


                
