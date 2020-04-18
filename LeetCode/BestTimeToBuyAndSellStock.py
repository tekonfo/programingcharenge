class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 左から順に見ていって、そのときに買える値の最高値を記録する
        max_prices = []
        for price in reversed(prices):
            if len(max_prices) == 0:
                max_prices.insert(0, price)
                continue
            max_prices.insert(0, max(price, max_prices[0]))
        print(max_prices)
        # 完璧
        ans = 0
        for index in range(len(prices)):
            profit = max_prices[index] - prices[index]
            ans = max(ans, profit)
        return ans
            
            
        
            
        