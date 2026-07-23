class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        l = []
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        for k, v in d.items():
            if v > n/3:
                l.append(k)
        return l