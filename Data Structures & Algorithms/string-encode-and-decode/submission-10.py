class Solution:
    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs: 
            r = len(s) + s

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0 
        j = int(s[0]) + 1
        while j <= len(s):
            l.append(s[i:j])
            i = j + 1
            j = j + int(s[j]) + 1
        return l

