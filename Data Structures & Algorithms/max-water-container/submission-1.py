class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        i = 0
        j = len(heights) - 1
        m = (j-i)*min(heights[i], heights[j])
        while i <= j:
            area2 = (j-i-1)*min(heights[i+1], heights[j])
            if area2 > m: 
                m = area2
                i+=1
            else: 
                j-=1
            area3 = (j-i-1)*min(heights[i], heights[j-1])
            if area3 > m: 
                m = area3
                j-=1
            else: 
                i+=1
        return m

        