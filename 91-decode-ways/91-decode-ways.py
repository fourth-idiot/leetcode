class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def helper(s):
            if(s == ""):
                return 1
            elif(s in dp):
                return dp[s]
            else:
                for i in range(1, 27):
                    iStr = str(i)
                    if(s.startswith(iStr)):
                        dp[s] = dp.get(s, 0) + helper(s[len(iStr):])
                return dp.get(s, 0)
        return helper(s)