class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        has_zero = False
        for n in nums:
            if n == 0 and has_zero == True:
                return [0]*len(nums)
            elif n == 0:
                has_zero = True 
            else: 
                p *= n
        
        l = []
        for n in nums: 
            if has_zero and n==0:
                l.append(p)
            elif has_zero:
                l.append(0)
            else:
                l.append(p//n)
        return l
