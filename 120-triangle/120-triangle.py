class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp = [[0 for _ in range(len(triangle) + 1)] for _ in range(len(triangle[-1]) + 1)]
        # for i in range(len(triangle) - 1, -1, -1):
        #     for j in range(0, i + 1):
        #         dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        # return dp[0][0]
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(0, i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]