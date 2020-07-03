from typing import List
import itertools
INF = 100000000

class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    mi = 10000000
    ma = 0
    prev = nums[-1]
    for index in reversed(range(0, len(nums))):
      print(nums[index], prev)
      if (nums[index] < prev):
        print("hit! {}".format(nums[index]))
        t_max = 10000000
        for i in range(index, len(nums)):            
          if (nums[index] < nums[i] and t_max > nums[i]):
            print("change! {}".format(nums[i]))
            t_max = nums[i]
            max_index = i
        # まず入れ替える
        t = nums[max_index]
        nums[max_index] = nums[index]
        nums[index] = t
        print(nums)
        nums[index+1:] = reversed(nums[index+1:])
        print(nums)
        return
      prev = nums[index]
    #if num is largest in permutation, simply reverse        
    temp=[]
    temp[:]=nums[:]
    nums[:]=temp[::-1]

          
lists = [2,2,7,5,4,3,2,2,1]
sol = Solution()
sol.nextPermutation(lists)