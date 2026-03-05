class Solution:
    def maxProfit(self, prices):
        decision_table = {}
        buying_price = prices[0]
        max_profit  = 0
        if len(prices) < 2:
            return 0
        else:
            for idx in range(1, len(prices)):
                profit = prices[idx] - buying_price #4 - 2 #2, 1
                if profit > 0:
                    if profit > max_profit:
                        max_profit = profit
                else:
                    buying_price = prices[idx]
        return max_profit

prices = [7,6,4,3,1]
result  = Solution()
res = result.maxProfit(prices)
print(res)


