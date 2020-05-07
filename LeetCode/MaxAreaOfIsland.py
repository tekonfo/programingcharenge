from collections import deque
from typing import List

class Solution:
    def returnPoints(self, y, x):
        return [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid == None or len(grid) == 0:
            return 0

        ans = 0
        queue = deque()
        tmp = 0

        # 二重for文で端から順にみていく
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))

                # queue使って深さ優先探索で上下左右に島がないかをチェックする
                while len(queue) != 0:
                    a, b = queue.pop()
                    grid[a][b] = 0
                    
                    points = self.returnPoints(a, b) 
                
                    tmp += 1
                    for y, x in points:
                        if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 1:
                
                            queue.append((y, x))
                            grid[y][x] = 0
                    
    
                ans = max(ans, tmp)
                print(ans)
                tmp = 0

        return ans

sol = Solution()
grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]]

print(sol.maxAreaOfIsland(grid))