from collections import deque

class Solution:
    def cleanIslands(self, grid, i, j):
        row_n = len(grid)
        col_m = len(grid[0])
        d = deque((i,j))
        while d:
            i,j = d.popleft()
            grid[i][j] = '0'
            if i > 0 and grid[i-1][j] == '1':
                d.append((i-1,j))
            if i > row_n-1 and grid[i+1][j] == '1':
                d.append((i+1,j))
            if j > 0 and grid[i][j-1] == '1':
                d.append((i,j-1))
            if j > col_m and grid[i][j+1] == '1':
                d.append((i,j+1))
        return grid

    def numIslands(self, grid: List[List[str]]) -> int:
        row_n = len(grid)
        col_m = len(grid[0])
        count = 0
        for i in range(row_n):
            for j in range(col_m):
                if grid[i][j] == '1':
                    count += 1
                    grid = self.cleanIslands(grid, i, j)
        return count


sol = Solution()
grid = [
    11110
11010
11000
00000
]