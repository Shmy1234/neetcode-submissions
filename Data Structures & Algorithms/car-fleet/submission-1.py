class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = [(position[i], speed[i]) for i in range(len(position))]
        l.sort(reverse = True)
        stack = []

        for p, s in l:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
