class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + word 
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        code = int(s[0])
        s2 = '' 
        for i in range(1, len(s)):
            if len(s2) == code:
                code = int(s[i])
                l.append(s2)
                s2 = ''
            else:
                s2 += s[i]
        
        return l + [s2]
            
            

