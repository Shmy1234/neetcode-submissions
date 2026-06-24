class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for n in nums: 
            if n-1 in nums: 
                d[n] = 1 + d[n-1]
            else: 
                d[n] = 1
        
        return max(list(d.values()))