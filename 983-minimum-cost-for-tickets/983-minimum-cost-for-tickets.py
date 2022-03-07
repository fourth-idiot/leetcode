class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = max(days)
        dp = [0 for _ in range((maxDay+30)+1)]
        for i in range(maxDay, 0, -1):
            if(i not in days):
                dp[i] = dp[i+1]
            else:
                dp[i] = min(
                    costs[0] + dp[i+1],
                    costs[1] + dp[i+7],
                    costs[2] + dp[i+30]
                )
        return dp[1]