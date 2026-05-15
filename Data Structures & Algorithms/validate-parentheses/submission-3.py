class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in ")}]":
                if stack and stack[-1]==d[char]:
                    stack.pop()
                else:
                    return False
            elif char in "([{":
                stack.append(char)
        return stack==[]