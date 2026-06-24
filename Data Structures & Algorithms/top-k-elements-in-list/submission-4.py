class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n] = 1 + d.get(n, 0)
        l = []
        for key, val in d.items():
            l.append((val, key))
        l.sort()
        l2 = []
        for i in range(k):
            l2.append(l.pop()[1])
        return l2