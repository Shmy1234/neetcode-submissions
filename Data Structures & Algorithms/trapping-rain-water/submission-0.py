class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left, right = height[l], height[r]
        rain = 0

        while l<r:
            if left < right:
                l+=1
                left = max(left, height[l])
                rain += left - height[l]
            else:
                r-=1
                right = max(right, height[r])
                rain += right - height[r]

        return rain 