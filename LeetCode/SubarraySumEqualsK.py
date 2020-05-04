from typing import List
import bisect

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        for 

        
sol = Solution()
nums = [1,1,1]
k = 2
sol.subarraySum(nums, k)