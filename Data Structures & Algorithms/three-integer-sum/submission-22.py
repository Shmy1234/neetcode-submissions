class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k: 
                l = [nums[i], nums[j], nums[k]]
                r = nums[i] + nums[j] + nums[k]
                if r == 0:
                    if l not in res:
                        res.append(l)
                    j+=1
                    k-=1
                elif r < 0:
                    j+=1
                else:
                    k-=1
        
        return res

                
