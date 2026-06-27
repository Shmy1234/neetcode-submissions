class Solution:
    def isValid(self, s: str) -> bool:
        t = {"}":"{", "]":"[",")":"("}
        stack = []
        for c in s: 
            if c in t and stack!=[] and stack.pop() == t[c]:
                continue
            elif c in "[({":
                stack.append(c)
            else: 
                return False
        return True