class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "-":
                l = stack.pop()
                stack[-1] = stack[-1] - l
            elif char == "+":
                l = stack.pop()
                stack[-1] = stack[-1] + l
            elif char == "*":
                l = stack.pop()
                stack[-1] = stack[-1] * l
            elif char == "/":
                l = stack.pop()
                stack[-1] = math.trunc(stack[-1]/l)
            else:
                if char == "0":
                    stack.append(0)
                else:
                    stack.append(int(char))
        
        return stack[0]
        