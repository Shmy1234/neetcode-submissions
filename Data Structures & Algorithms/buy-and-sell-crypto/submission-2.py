class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        if len(prices) < 2:
            return 0
        max_profit = 0
        while j < len(prices) and i < len(prices):
            if prices[j] < prices[i]:
                i += j
                j += 1
            else:
                max_profit = max(max_profit, prices[j] - prices[i])
                j+=1

        return max_profit

        

        