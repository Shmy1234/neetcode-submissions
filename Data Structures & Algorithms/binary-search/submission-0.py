class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        m = j//2
        while i <= len(nums)-1 and j > 0:
            m = (i + j)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                i = i + m
            elif target < nums[m]:
                j = j - m - 1
        
        return -1

            
