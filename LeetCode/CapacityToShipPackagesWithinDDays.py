# import bisect
# from typing import List

# class Solution:
#     def toubun(self, x, n):
#         l = [(x + i) // n for i in range(n)]
#         return l

#     def shipWithinDays(self, weights: List[int], D: int) -> int:
#         sums = [0]
#         #　まず、累積和を求める
#         for index in range(len(weights)):
#             sums.append(weights[index] + sums[index])
        
#         # 等分配列を入手
#         lists = self.toubun(sums[-1], D)
#         print(lists)

#         # それぞれの数字に対して適切な挿入場所を検索する
#         ans = 0
#         prev_index = 0
#         for c in lists:
#             index = bisect.bisect_left(sums, c, prev_index, len(sums)+1)
#             # インデックスで、より近い方に挿入する
#             if index > 0 and abs(sums[index] - c) >= abs(sums[index-1] - c):
#                 index = index - 1
#             s = sums[index] - sums[prev_index]
#             ans = max(ans, s)
#         return ans

# sol = Solution()
# weights = [1,2,3,4,5,6,7,8,9,10]
# D = 5
# print(sol.shipWithinDays(weights, D))

"""
The intuition for this problem, stems from the fact that

a) Without considering the limiting limiting days D, if we are to solve, the answer is simply max(a)
b) If max(a) is the answer, we can still spend O(n) time and greedily find out how many partitions it will result in.

[1,2,3,4,5,6,7,8,9,10], D = 5

For this example, assuming the answer is max(a) = 10, disregarding D,
we can get the following number of days:
[1,2,3,4] [5] [6] [7] [8] [9] [10]

So by minimizing the cacpacity shipped on a day, we end up with 7 days, by greedily chosing the packages for a day limited by 10.

To get to exactly D days and minimize the max sum of any partition, we do binary search in the sum space which is bounded by [max(a), sum(a)]

Binary Search Update:
One thing to note in Binary Search for this problem, is even if we end up finding a weight, that gets us to D partitions, we still want to continue the space on the minimum side, because, there could be a better minimum sum that still passes <= D paritions.

In the code, this is achieved by:

if res <= d:
     hi = mid
With this check in place, when we narrow down on one element, lo == hi, we will end up with exactly the minimum sum that leads to <= D partitions.
"""
from typing import List

def shipWithinDays(self, a: List[int], d: int) -> int:
        lo, hi = max(a), sum(a)   
        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for wt in a:
                if tot + wt > mid:
                    res += 1
                    tot = wt
                else:
                    tot += wt
            if res <= d:
                hi = mid
            else:
                lo = mid+1
        return lo


            




        
        
