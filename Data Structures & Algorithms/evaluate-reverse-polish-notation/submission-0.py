class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = int(tokens[0])
        for i in range(2, len(tokens), 2):
            if tokens[i] == '+':
                num += int(tokens[i-1])
            if tokens[i] == '-':
                num -= int(tokens[i-1])
            if tokens[i] == '/':
                num = round(num/int(tokens[i-1]))
            if tokens[i] == '*':
                num *= int(tokens[i-1])
        return num
            
        