class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + ' '+ s
        return res

    def decode(self, s: str) -> List[str]:
        res = [] #4 band0 2 at
        i = 0
        num = ''
        while i < len(s):
            if s[i] != ' ':
                num += s[i]
                i += 1
            else:
                res.append(s[i + 1: i + 1 + int(num)])
                i = i + 1 + int(num)
                num = ''
        return res





