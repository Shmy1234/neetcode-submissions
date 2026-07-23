class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue 
            k = i + 1 
            j = len(nums) - 1
            while k < j:
                e = [nums[i], nums[k], nums[j]]
                num = nums[i] + nums[k] + nums[j]
                if num > 0:
                    j -= 1
                elif num < 0:
                    k += 1
                else:
                    if e not in l:
                        l.append(e)
                k += 1
                j -= 1
        
        return l

    
