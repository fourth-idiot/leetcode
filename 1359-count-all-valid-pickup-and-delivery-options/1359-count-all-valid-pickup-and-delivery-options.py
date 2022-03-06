class Solution:
    def countOrders(self, n: int) -> int:
        mod = 1_000_000_000 + 7
        dp = {}
        def helper(unpicked, undelivered):
            key = "up{}ud{}".format(unpicked, undelivered)
            if((unpicked == 0) and (undelivered == 0)):
                dp[key] = 1
                return 1
            elif((unpicked < 0) or (undelivered < 0) or (undelivered < unpicked)):
                return 0
            elif(key in dp):
                return dp[key]
            else:
                ans = unpicked * helper(unpicked-1, undelivered)
                ans += (undelivered - unpicked) * helper(unpicked, undelivered-1)
                ans %= mod
                dp[key] = ans
                return ans
        return helper(n, n)