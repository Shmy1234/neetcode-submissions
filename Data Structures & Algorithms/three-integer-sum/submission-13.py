class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i]+nums[j]+nums[k]
                l2 = [nums[i], nums[j], nums[k]]
                l2.sort()
                if s == 0 and l2 not in l:
                    l.append(l2)
                elif s < 0: 
                    j += 1
                elif s > 0: 
                    k -= 1
                else:
                    i += 1
        
        return l
