from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))] 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # every loop, calculate the maximum cumulative amount of money until current house
        for i in range(2,len(nums)):
            # as the loop begins，curr represents dp[k-1]，prev represents dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + i }
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            # as the loop ends，curr represents dp[k]，prev represents dp[k-1]

        return dp[-1]

nums = [3,1,1,3]
sol = Solution()
print(sol.rob(nums))