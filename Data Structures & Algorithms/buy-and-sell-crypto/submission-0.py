class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')   # cheapest price seen so far
        max_profit = 0             # best profit found so far

        for price in prices:
            if price < min_price:
                min_price = price          # found a cheaper day to buy
            elif price - min_price > max_profit:
                max_profit = price - min_price   # selling today beats our record

        return max_profit