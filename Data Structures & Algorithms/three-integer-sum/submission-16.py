class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        l = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                n = nums[i] + nums[j] + nums[k]
                res = [nums[i], nums[j], nums[k]]
                if n > 0:
                    k -= 1
                if n < 0: 
                    j +=1
                elif n == 0 and res not in l:
                        l.append(res)
                k-=1 
                j+=1
            
        return l