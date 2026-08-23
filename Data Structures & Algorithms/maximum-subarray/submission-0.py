class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = nums[0]
        c = 0
        for n in nums: 
            c = max(c, 0) + n
            m = max(m, c)
        return m