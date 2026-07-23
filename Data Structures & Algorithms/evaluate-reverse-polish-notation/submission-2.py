from math import floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = int(tokens[0])
        stack = [tokens[0]]
        for i in range(1,len(tokens)):
            print(stack, num)
            if tokens[i].isdigit():
                stack.append(tokens[i])
            if tokens[i] == "+":
                num = num + int(stack[-1])
                stack.pop()
            if tokens[i] == "-":
                num = num - int(stack[-1])
                stack.pop()
            if tokens[i] == "*":
                num = num * int(stack[-1])
                stack.pop()
            if tokens[i] == "/":
                num = math.floor(num/int(stack[-1]))
                stack.pop()
        
        return num
            
            
        