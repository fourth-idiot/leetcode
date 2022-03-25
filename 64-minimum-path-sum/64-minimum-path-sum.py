class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        dp = [[0 for _ in range(numCols)] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(numCols):
                if((i == 0) and (j == 0)):
                    dp[i][j] = grid[i][j]
                elif(i == 0):
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif(j == 0):
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(
                        dp[i][j-1],
                        dp[i-1][j]
                    )
        return dp[-1][-1]