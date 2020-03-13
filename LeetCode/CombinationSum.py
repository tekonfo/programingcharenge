from typing import List
import copy

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    arrs = []
    arr = [[] for i in range(target+1)]
    arr[0] = [[0]]
    for item in candidates:  
      # target + 1個の配列を作成する
      for index in range(len(arr)):
        if len(arr[index]) >= 1 and index + item <= target:
          for pair in arr[index]:
            tmp = copy.deepcopy(pair)
            tmp.append(item)
            arr[index+item].append(tmp)
      print(arr)
    anss = arr[-1]
    for ans in anss:
      ans.remove(0)

    return anss


        

candidates = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))