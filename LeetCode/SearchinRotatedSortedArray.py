from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) >> 1
      print(mid)
      if nums[mid] == target:
        return mid
      
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid -1
    return -1
    

lists = [1,3,5,6]
target = 2
sol = Solution()
print(sol.nextPermutation(lists, target))