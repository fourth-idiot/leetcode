class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # Approach using 2D dp matrix
        # dp = [[float("inf") for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # # Initialize the first column with 0 as we need 0 coins to make 0 amount
        # for i in range(len(coins) + 1):
        #     dp[i][0] = 0
        # # Calculate the DP matrix
        # for i in range(1, len(coins) + 1):
        #     for j in range(1, amount + 1):
        #         if(j >= coins[i - 1]):
        #             dp[i][j] = min(
        #                 dp[i - 1][j],
        #                 1 + dp[i][j - coins[i - 1]]
        #             )
        #         else:
        #             dp[i][j] = dp[i - 1][j]
        # return -1 if (dp[-1][-1] == float("inf")) else dp[-1][-1]
    
        # Approach using 1D dp matrix
        dp = [float("inf") for _ in range(amount + 1)]
        # Initialize the value with 0 as we need 0 coins to make 0 amount
        dp[0] = 0
        # Calculate the DP matrix
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if(j >= coins[i - 1]):
                    dp[j] = min(dp[j], 1 + dp[j - coins[i - 1]])
        return -1 if (dp[-1] == float("inf")) else dp[-1]