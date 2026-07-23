class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for num in nums:
            v = list(d.items())
            print(v)
            if num - 1 in d:
                d[num] = 1 + d[num-1]
            else:
                d[num] = 1
        v = list(d.values())
        return max(v)
        
        