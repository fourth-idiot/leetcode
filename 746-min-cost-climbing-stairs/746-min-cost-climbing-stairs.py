class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost) + 1)]
        for i in range(2, len(dp)):
            dp[i] = min(
                dp[i - 2] + cost[i - 2],
                dp[i - 1] + cost[i - 1]
            )
        return dp[-1]
        
        # # With state reduction
        # secondLast, last = 0, 0
        # for i in range(2, len(cost) + 1):
        #     current = min(
        #         secondLast + cost[i - 2],
        #         last + cost[i - 1]
        #     )
        #     secondLast = last
        #     last = current
        # return last