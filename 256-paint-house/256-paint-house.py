class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n, numColors = len(costs), 3
        dp = [[0 for _ in range(3)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i][0] = costs[i][0] + min(dp[i + 1][1], dp[i + 1][2])
            dp[i][1] = costs[i][1] + min(dp[i + 1][0], dp[i + 1][2])
            dp[i][2] = costs[i][2] + min(dp[i + 1][0], dp[i + 1][1])
        return min(dp[i])