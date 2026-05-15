class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}":"{", "]":"[", ")":"("}
        stack = []
        for char in s:
            if char in "{([":
                stack.append(char)
            elif char in d:
                if not stack or stack.pop()!= d[char]:
                    return False
        
        return not stack