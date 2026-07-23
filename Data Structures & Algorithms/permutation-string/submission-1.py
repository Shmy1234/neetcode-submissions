class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1, d2, = {}, {}
        i, j = 0, len(s1) - 1
        for c in range(len(s1)):
            d1[s1[c]] = 1 + d1.get(s1[c],0)
            d2[s1[c]] = 0 + d2.get(s1[c],0)
        for c in range(len(s1)):
            if s2[c] in d1:
                d2[s2[c]] = 1 + d2.get(s2[c],0)

        while j < len(s2):
            print(s1, s2[i:j+1], d1, d2)
            if d1 == d2:
                return True 
            else:
                if s2[i] in d2:
                    d2[s2[i]] -= 1
                i+=1 
                j+=1
                if j < len(s2) and s2[j] in d2:
                    d2[s2[j]] += 1
        
        return False


            
        