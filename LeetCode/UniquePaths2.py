from typing import List
import sys
class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    maps = []
    # 障害を-1に設定する。
    for grid in obstacleGrid:
      maps.append([-1 if x == 1 else 0 for x in grid])

    n = len(obstacleGrid)
    m = len(obstacleGrid[0])

    if maps[0][0] == -1:
      return 0

    maps[0][0] = 1
    for map_index in range(n):
      for point_index in range(m):
        if maps[map_index][point_index] == -1:
          continue

        # 上をみて数字があるならたす
        if map_index - 1 >= 0 and maps[map_index-1][point_index] != -1:
          maps[map_index][point_index] += maps[map_index-1][point_index]
         
        # 左をみて数字があるならたす
        if point_index - 1 >= 0 and maps[map_index][point_index-1] != -1:
          maps[map_index][point_index] += maps[map_index][point_index-1]
      
    return maps[n-1][m-1] if maps[n-1][m-1] >= 0 else 0


g = [
  [0,1]
]   
sol = Solution()
print(sol.uniquePathsWithObstacles(g))