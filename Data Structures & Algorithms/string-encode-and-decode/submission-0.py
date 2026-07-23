class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + s
        return res

    def decode(self, s: str) -> List[str]:
        l = []
        res = ''
        skip = 0
        for i, char in enumerate(s):
            if i == 0:
                skip = int(char) + 1
            else:
                if i == skip:
                    l.append(res)
                    res = ''
                    skip += int(char) + 1
                else:
                    res += char

            if i == len(s) - 1:
                l.append(res)

        return l




