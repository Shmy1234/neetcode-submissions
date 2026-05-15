class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        dT, w = {}, {}
        for c in t:
            dT[c] = 1 + dT.get(c, 0)

        have, need = 0, len(dT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        r = 0
        while r < len(s):
            c = s[r]
            w[c] = 1 + w.get(c, 0)

            if c in dT and w[c] == dT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                w[s[l]] -= 1
                if s[l] in dT and w[s[l]] < dT[s[l]]:
                    have -= 1
                l += 1
            
            r += 1
        
        if resLen != float("infinity"):
            return s[res[0] : res[1] + 1] 
        
        return ""


                
