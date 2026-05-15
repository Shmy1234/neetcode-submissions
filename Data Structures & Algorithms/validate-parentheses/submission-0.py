class Solution:
    def isValid(self, s: str) -> bool:
        tracker = {')': '(',']': '[','}': '{'}
        stack = []
        for char in s:
            if char in ')]}':
                if not stack or stack[-1] != tracker[char]:
                    return False
                else:
                    stack.pop()
            elif char in '([{':
                stack.append(char)

        return not stack

        
        