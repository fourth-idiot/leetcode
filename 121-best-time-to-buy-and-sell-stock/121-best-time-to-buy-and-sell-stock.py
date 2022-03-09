class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPriceTillNow = float("inf")
        for price in prices:
            if(price < lowestPriceTillNow):
                lowestPriceTillNow = price
            else:
                profit = price - lowestPriceTillNow
                maxProfit = max(maxProfit, profit)
        return maxProfit