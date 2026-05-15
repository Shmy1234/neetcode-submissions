class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(n):
            if n == len(nums):
                if len(sol[:]) == len(nums):
                    res.append(sol[:])
                return None
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack(n+1)
                    sol.pop()
        
        backtrack(0)

        return res
            
