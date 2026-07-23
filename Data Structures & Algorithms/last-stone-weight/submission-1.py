class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        i = len(stones) - 2
        j = len(stones) - 1
        while len(stones) > 1:
            if stones[i] == stones[j]:
                stones.pop()
                stones.pop()
                i-=2
                j-=2
            elif stones[i] < stones[j]:
                stones[j] -= stones[i]
                stones.pop(i)
                i-=1
                j-=1
            else:
                stones[i] -= stones[j]
                stones.pop(j)
                i-=1
                j-=1

        if stones == []:
            return 0
        return stones[0]
            

        