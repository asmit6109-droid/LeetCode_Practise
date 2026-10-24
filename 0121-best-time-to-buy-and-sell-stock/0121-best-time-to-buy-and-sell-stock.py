class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit = 0
        bestbuy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > bestbuy:
                maxprofit = max(maxprofit,prices[i]-bestbuy)
            
            bestbuy = min(bestbuy,prices[i])
        return maxprofit