class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        minPrice = float("inf")
        for price in prices:
            if(price < minPrice):
                minPrice = price
            else:
                output = max(output, price - minPrice)
        return output