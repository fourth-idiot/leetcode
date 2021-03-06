class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Approach (Using tabulation):
        # This problem is similar to the house robber problem in which
        # we have to maximize the money we can rob without robbing adjacent houses.
        # Here if we color house 1 with red color, then house 2 cannot be colored with red.
        # Hence, the cost of painting house 1 with red color can be calculated as following:
        # dp[1][0] = cost[1][1] + min(dp[2][1] + dp[2][2])
        # Finally, minimum value of dp[1][0], dp[1][1], and dp[1][2]
        # will be the minimum cost to paint all houses starting house 1.
        
        # In our problem, we have only 3 options to color our houses,
        # but we will try to make code as generalized as possible.
        n, numColors = len(costs), 3
        dp = [[0 for _ in range(numColors)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(numColors):
                dp[i][j] = costs[i][j] + min(dp[i + 1][:j] +  dp[i + 1][j + 1:])
        return min(dp[i])