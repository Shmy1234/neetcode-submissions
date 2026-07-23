class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res = res + str(len(s)) + s
        return res

    def decode(self, s: str) -> List[str]:
        if s == "0":
            return [""]
        if s == "":
            return []

        c = int(s[0])
        l = []
        i = 0
        while i < len(s):
            c = int(s[i])
            i+=1
            l.append(s[i:i+c])
            i += c 
        return l

