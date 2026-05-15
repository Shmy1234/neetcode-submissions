class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, profit, best = 0, 0, 0, 0
        while j <= len(prices) - 1:
            print(best)
            if i == j:
                j +=1
            elif prices[i] > prices[j]:
                i += 1
            else:
                profit = prices[j] - prices[i]
                if profit > best:
                    best = profit
                j += 1
        
        return best
        