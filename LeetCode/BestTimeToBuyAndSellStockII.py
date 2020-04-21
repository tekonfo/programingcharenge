from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_v = 0
        max_v = 0
        search_min = True
        ans = 0
        for index in range(len(prices)-1):
            if search_min:
                if prices[index] < prices[index+1]:
                    min_v = prices[index]
                    search_min = False
            else:
                if prices[index] > prices[index+1]:
                    max_v = prices[index]
                    ans += max_v - min_v
                    search_min = True
        
        if not search_min:
            ans += prices[-1] - min_v
            
        return ans

sol = Solution()
lists = [7,1,5,3,6,4]
print(sol.maxProfit(lists))