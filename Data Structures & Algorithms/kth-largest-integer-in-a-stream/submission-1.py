class KthLargest:
    k: int 
    nums: List[int]
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        n = self.nums.copy()
        n.sort()
        return n[-self.k]
        
