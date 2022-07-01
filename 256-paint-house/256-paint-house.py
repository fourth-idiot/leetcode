class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n, numColors = len(costs), 3
        dp = [[0 for _ in range(numColors)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(numColors):
                dp[i][j] = costs[i][j] + min(dp[i + 1][:j] +  dp[i + 1][j + 1:])
        return min(dp[i])