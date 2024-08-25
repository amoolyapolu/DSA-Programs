"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price=prices[0]
        current_profit = 0
        for i in prices:
            if i < buy_price: 
                buy_price = i
            else:
                current_profit = i - buy_price #7-7
                profit = max(current_profit,profit)
        return profit
