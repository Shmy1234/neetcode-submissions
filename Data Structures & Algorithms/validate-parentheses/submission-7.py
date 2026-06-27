class Solution:
    def isValid(self, s: str) -> bool:
        t = {"}":"{", "]":"[",")":"("}
        stack = []
        for c in s: 
            if c in "[({":
                stack.append(c)
            elif c in t: 
                if stack==[] or stack.pop()!=t[c]:
                    return False
        
        return stack==[]