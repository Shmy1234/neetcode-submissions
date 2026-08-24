class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        m = 0
        while j < len(prices) - 1:
            if prices[j] < prices[i]:
                i = j 
                j+=1
            else:
                j+=1
            m = max(m, prices[j] - prices[i])
        
        return m
