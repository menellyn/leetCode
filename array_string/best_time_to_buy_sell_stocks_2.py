class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_profit, profit = 0, 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy and profit == 0:
                buy = prices[i]
            elif prices[i] - buy  > profit:
                profit = prices[i] - buy
            else:
                global_profit += profit
                profit = 0
                buy = prices[i]