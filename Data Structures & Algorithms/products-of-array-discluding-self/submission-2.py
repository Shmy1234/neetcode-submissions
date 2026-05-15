class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zero_exists = False
        for n in nums:
            if zero_exists and n == 0:
                return [0]*len(nums)
            elif n == 0:
                zero_exists = True 
            else:
                p *= n 
        l = []
        for n in nums:
            if n == 0:
                l.append(p)
            elif zero_exists:
                l.append(0)
            else:
                l.append(p//n)
        return l
        