from typing import List
import copy

class Solution:
  def onePermute(self, unused: List[int], used: List[int]) -> List[List[int]]:
    if len(unused) == 0:
      return [used]

    lists = []
    for a in unused:
      tmp_used = copy.deepcopy(used)
      tmp_used.append(a)
      tmp_unsed = copy.deepcopy(unused)
      tmp_unsed.remove(a)
      tmp_list = self.onePermute(tmp_unsed, tmp_used) 
      for l in tmp_list:
        lists.append(l)
    return lists

  def permute(self, nums: List[int]) -> List[List[int]]:
    return self.onePermute(nums, [])

lists = [1,3,5,6]
sol = Solution()
print(list(sol.permute(lists)))