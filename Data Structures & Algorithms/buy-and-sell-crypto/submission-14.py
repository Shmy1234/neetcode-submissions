class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        m = 0
        while j < len(prices):
            m = max(m, prices[j] - prices[i])
            if i == j:
                j+=1
            if prices[j] < prices[i]:
                i = j 
            else:
                j+=1
        
        return m
