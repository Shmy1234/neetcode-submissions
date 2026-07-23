class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[nums.count(num)] = num
        l = list(d.items())
        l.sort()
        l2 = []
        for i in range(k):
            l2.append(l.pop()[1])
        return l2