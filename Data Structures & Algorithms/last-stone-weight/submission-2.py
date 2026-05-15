class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            curr = stones.pop() - stones.pop()
            if curr != 0:
                stones.append(abs(curr))

        if stones == []:
            return 0
        return stones[0]
            

        