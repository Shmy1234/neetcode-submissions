class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""

        res = ""
        for s in strs: 
            res = res + str(len(s)) + s
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]

        c = int(s[0])
        l = []
        i = 1
        while i < len(s):
            c = int(s[i - 1])
            l.append(s[i:i+c])
            i += c + 1
        return l

