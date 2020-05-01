from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        print(sums)
        
sol = Solution()
nums = [1,1,1]
k = 2
sol.subarraySum(nums, k)