class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', ']':'[', '}':"{"}
        stack = []
        for char in s:
            print(stack, char)
            if char in d:
                if d[char] not in stack.pop():
                    return False
            else:
                stack.append(char)
        return True