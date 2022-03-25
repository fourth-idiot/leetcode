class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        numRows, numCols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(numCols)] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(numCols):
                if(i == 0):
                    dp[i][j] = matrix[i][j]
                elif(j == 0):
                    dp[i][j] = matrix[i][j] + min(
                        dp[i-1][j],
                        dp[i-1][j+1]
                    )
                elif(j == (numCols - 1)):
                    dp[i][j] = matrix[i][j] + min(
                        dp[i-1][j-1],
                        dp[i-1][j]
                    )
                else:
                    dp[i][j] = matrix[i][j] + min(
                        dp[i-1][j-1],
                        dp[i-1][j],
                        dp[i-1][j+1]
                    )
        return min(dp[-1])