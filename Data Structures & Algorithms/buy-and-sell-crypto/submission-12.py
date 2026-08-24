class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        m = 0
        while j < len(prices) - 1:
            if prices[j] > prices[i]:
                m = max(m, prices[j] - prices[i])
            else:
                i=j
            j+=1
        
        return m
