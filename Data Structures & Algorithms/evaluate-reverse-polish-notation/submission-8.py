import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            print(stack)
            if char == "+":
                last = stack.pop()
                stack[-1] = stack[-1] + last
            elif char == "-":
                last = stack.pop()
                stack[-1] = stack[-1] - last
            elif char == "*":
                last = stack.pop()
                stack[-1] = stack[-1] * last
            elif char == "/":
                last = stack.pop()
                n = stack[-1]/last
                stack[-1] = math.trunc(n)
            elif int(char) or char == '0':
                stack.append(int(char))
        return stack[0]
            
            
            
        