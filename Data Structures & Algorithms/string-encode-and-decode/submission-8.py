class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + " " + s
        return res

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != " ":
                j+=1
            c = int(s[i:j])
            i = j + 1
            j += i + c
            l.append(s[i:j])
            i = j
        return l
