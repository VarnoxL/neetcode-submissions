class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time o(n)
        #space o(1)
        #ensure first element in price list smaller than min_price
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
