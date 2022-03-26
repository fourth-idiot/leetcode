class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # # Approach 1
        # dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # for i in range(1, len(dp)):
        #     dp[i][0] = 1
        # for i in range(1, len(dp)):
        #     for j in range(1, len(dp[0])):
        #         dp[i][j] = dp[i - 1][j]
        #         if(j >= coins[i - 1]):
        #             dp[i][j] += dp[i][j - coins[i - 1]]
        # return dp[-1][-1]
        
        # Approach 2: Using state reduction
        row = [0 for _ in range(amount + 1)]
        row[0] = 1
        for coin in coins:
            for j in range(1, len(row)):
                if(j >= coin): row[j] += row[j - coin]
        return row[-1]
        