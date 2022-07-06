class Solution:
    def fib(self, n: int) -> int:
        # # Approach 1 (Recursion)
        # if((n == 0) or (n == 1)):
        #     return n
        # else:
        #     return self.fib(n - 1) + self.fib(n - 2)
        
        # Approach 2 (Dynamic programming - Memoization)
        dp = {0: 0, 1: 1}
        def helper(n):
            if(n in dp):
                return dp[n]
            return dp.get(n - 1, helper(n - 1)) + dp.get(n - 2, helper(n - 2))
        return helper(n)
    
        # # Approach 3 (Dynamic programming - Tabulation)
        # if((n == 0) or (n == 1)):
        #     return n
        # dp = [0 for _ in range(n + 1)]
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]