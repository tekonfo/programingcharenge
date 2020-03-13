from typing import List
import itertools
INF = 100000000

class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n_val = int(''.join([str(i) for i in nums]))
    ans_val = INF
    nGreatNums = nums
    allPatterns = itertools.permutations(nums)
    for pat in allPatterns:
      p_val = int(''.join([str(i) for i in pat]))
      if n_val < p_val and p_val < ans_val:
        print("test2")
        ans_nums = pat
        ans_val  = p_val

    if 'ans_nums' in locals():
      print("tests")
      for index, val in enumerate(ans_nums):
        nums[index] = val
    else:
      nums.sort()
    print(nums)


lists = [2,2,7,5,4,3,2,2,1]
sol = Solution()
sol.nextPermutation(lists)
    