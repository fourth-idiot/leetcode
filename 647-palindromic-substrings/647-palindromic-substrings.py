class Solution:    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            count += 1
        for j in range(n):
            for i in range(j):
                if(s[i] == s[j]):
                    if((i+1==j) or (dp[i+1][j-1])):
                        dp[i][j] = True
                        count += 1
        return count