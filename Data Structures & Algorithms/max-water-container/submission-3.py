class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        m = 0
        while i < j: 
            water = (j-i)*min(heights[i], heights[j])
            m = max(m, water)
            if heights[i] > heights[j]: 
                j-=1
            else: 
                i+=1 
        
        return m