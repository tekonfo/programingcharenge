from typing import List
from bisect import bisect_left

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 10000000
        sums = []
        sums.append(0)
        for i in range(len(nums)):
            sums.append(sums[i]+nums[i])

        print(sums)
        
        for i in range(1, len(sums)):
            to_find = s + sums[i-1]
            bound = bisect_left(sums, to_find)
            if bound == len(sums) and to_find > sums[-1]:
                continue
            ans = min(ans, bound - (i-1))

        return ans if ans != 10000000 else 0
    
sol = Solution()
s = 11
nums = [1,2,3,4,5]
print(sol.minSubArrayLen(s,nums))