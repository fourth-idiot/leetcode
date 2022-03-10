class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [float("inf") for _ in range(amount+1)]
        DP[0] = 0
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if(j >= coins[i]):
                    DP[j] = min(DP[j], (1 + DP[j-coins[i]]))
        opt = DP[amount] if (DP[amount] != float("inf")) else -1
        return opt