class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = max(days)
        dp = {}
        for i in range(maxDay, 0, -1):
            if(i not in days):
                dp[i] = dp[i+1]
            else:
                dp[i] = min(
                    costs[0] + dp.get(i+1, 0),
                    costs[1] + dp.get(i+7, 0),
                    costs[2] + dp.get(i+30, 0)
                )
        return dp[1]