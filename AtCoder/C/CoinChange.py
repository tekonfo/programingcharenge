from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(amount)]
        for coin in coins:
            dp[coin-1] = 1
            for i in range(amount):
                if dp[i] >= 1 and i+coin < amount:
                    if dp[i+coin] == 0:
                        dp[i+coin] = dp[i] + 1
                    else:
                        dp[i+coin] = min(dp[i] + 1, dp[i+coin])        
        return dp[-1] if dp[-1] != 0 else -1

                    
            
sol = Solution()
coins = [2]
amount = 3
print(sol.coinChange(coins, amount))