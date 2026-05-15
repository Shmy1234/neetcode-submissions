class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for num in nums:
            if num-1 in d:
                d[num] = 1 + d[num-1]
            elif num not in d:
                d[num] = 1
        val = list(d.values())
        if val: return max(val)
        else: return 0
