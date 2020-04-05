from typing import List

"""
Subarrayって繋がってなくてもいいらしい！！！
じゃあ下の回答間違ってるよな
"""

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    # とりあえず累積和を計算する
    tmp = 0
    add_array = []
    for i, num in enumerate(nums):
      tmp += num
      add_array.append(tmp)
    left_sum = 0
    ans = -10**10
    for i in range(len(nums)):
      tmp_array = add_array[i:]
      if i > 0:
        left_sum += nums[i-1]
      max_num = max(tmp_array)
      ans = max(ans, max_num - left_sum)
    return ans

if __name__ == '__main__':
  c = Solution()
  print(c.maxSubArray([-1]))