class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if((i < 0) or (i >= numRows) or
               (j < 0) or (j >= numCols) or
               (not grid[i][j])):
                return 0
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        
        numRows, numCols = len(grid), len(grid[0])
        maxArea = 0
        for i in range(numRows):
            for j in range(numCols):
                if(grid[i][j]):
                    area = dfs(i, j)
                    if(area > maxArea):
                        maxArea = area
        return maxArea