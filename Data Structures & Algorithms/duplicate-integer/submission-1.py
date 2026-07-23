class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return False
            s.add(num)
        return True   