class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
            if d[n] > len(nums)/2:
                return n 