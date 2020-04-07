class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    # map作成して足し合わせたらいける、一番上の左端からどんどん足していく感じにするか
    maps = [[0 for _ in range(m)] for _ in range(n)]
    maps[0][0] = 1
    for map_index in range(n):
      for point_index in range(m):
        # 上をみて数字があるならたす
        if map_index - 1 >= 0:
          maps[map_index][point_index] += maps[map_index-1][point_index]
         
        #
        if point_index - 1 >= 0:
          maps[map_index][point_index] += maps[map_index][point_index-1]
    return maps[n-1][m-1]


m = 1  
n = 1      
sol = Solution()
print(sol.uniquePaths(m,n))