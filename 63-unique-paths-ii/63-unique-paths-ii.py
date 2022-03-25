class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        numRows, numCols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(numCols)] for _ in range(numRows)]
        if(obstacleGrid[0][0] == 0):
            dp[0][0] = 1
        for i in range(numRows):
            for j in range(numCols):
                if(obstacleGrid[i][j]):
                    continue
                if(i > 0):
                    dp[i][j] += dp[i-1][j]
                if(j > 0):
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]