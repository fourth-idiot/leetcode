class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [[0, 0] for _ in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            # Cost to make the substring starting from index i monotonic
            if(s[i] == "0"):
                dp[i][0] = dp[i+1][0]
            else:
                dp[i][0] = min(
                    1 + dp[i+1][0],
                    dp[i+1][1]
                )
            # Cost to make the substring starting from index i string of all ones
            if(s[i] == "0"):
                dp[i][1] = 1 + dp[i+1][1]
            else:
                dp[i][1] = dp[i+1][1]
        return dp[0][0]