class Solution:
    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs: 
            r = r + str(len(s)) + s
        return r

        #4aand3app1q

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        l = []
        i = 1
        j = int(s[0]) + 1
        while j < len(s):
            l.append(s[i:j])
            i = j + 1
            j = j + int(s[j]) + 1
        
        l.append(s[i:j])

        return l

