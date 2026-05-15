class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        m = j//2
        while i <= j:
            m = (i + j + 1)//2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                j = m - 1
            else:
                i = m + 1
        
        return -1

            
