from typing import Union
class Solution:
    def subsets(self, nums: Union[int, List[int]]) -> List[List[int]]:
        res, sol = [], []
        def backtrack(n):
            if n == len(nums):
                res.append(sol[:])
                return 
            
            backtrack(n+1)

            sol.append(nums[n])
            backtrack(n+1)
            sol.pop()
        
        backtrack(0)
        return res
            
        