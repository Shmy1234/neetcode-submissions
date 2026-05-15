class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        l = []
        lst = []
        for key, value in d.items():
            l.append((value, key))
        l.sort()
        for i in range(k):
            lst.append(l.pop()[1])
        return lst

        



