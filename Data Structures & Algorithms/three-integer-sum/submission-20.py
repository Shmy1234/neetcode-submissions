class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1 
            while j < k:
                r = [nums[i], nums[j], nums[k]]
                t = nums[i] + nums[j] + nums[k]
                if t==0 and r not in res:
                    res.append(r)
                    j+=1 
                    k-=1
                elif t<0: 
                    j+=1
                else: 
                    k-=1
        return res
                    

