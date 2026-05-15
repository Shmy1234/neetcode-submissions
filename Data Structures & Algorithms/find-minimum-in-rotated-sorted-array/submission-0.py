class Solution:
    def findMin(self, nums: List[int]) -> int:
        i =  0
        j = len(nums) - 1
        while i < j:
            m = (i + j - 1) // 2
            if nums[j] > nums[m]:
                j = m 
            else:
                i = m + 1
        
        return nums[i]

