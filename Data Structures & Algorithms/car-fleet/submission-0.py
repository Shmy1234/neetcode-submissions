class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = set() 
        for i in range(len(position)):
            steps = (target - position[i]) // speed[i]
            if steps not in s:
                s.add(steps)
        
        return len(s)