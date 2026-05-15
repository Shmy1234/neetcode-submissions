class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, m = 0, len(height) - 1, 0
        while i<=j:
            if height[i] < height[j]:
                m = max(m, (j-i)*height[i])
                i+=1
            else:
                m = max(m, (j-i)*height[j])
                j-=1 
        
        return m 

        