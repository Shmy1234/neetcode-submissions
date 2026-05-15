class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        amount = 1
        zero_found = 0
        for num in nums:
            if num != 0:
                amount *= num
            else:
                zero_found += 1
        for num in nums:
            if zero_found > 1:
                res.append(0)
            elif zero_found == 1 and num == 0:
                 res.append(amount)
            elif zero_found == 1 and num != 0:
                res.append(0)
            else:
                res.append(int(amount/num))
        return res

        