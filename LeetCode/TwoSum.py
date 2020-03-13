from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # とりあえず全探索しよう
    for index, num in enumerate(nums):
      if index < len(nums) and target - num in nums[index+1:]:
        return [index, index + nums[index+1:].index(target-num) + 1]
      
sol = Solution()
n = [3,2,4]
t = 6

print(sol.twoSum(n,t))

