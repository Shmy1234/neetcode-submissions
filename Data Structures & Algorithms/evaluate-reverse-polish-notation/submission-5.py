from math import floor
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
                stack[-1] = int(math.floor(stack[-1]/last))
            elif int(char):
                stack.append(int(char))
        return stack[0]
            
            
            
        