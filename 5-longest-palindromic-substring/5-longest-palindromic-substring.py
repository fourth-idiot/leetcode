class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        output = ""
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            output = s[i]
        for j in range(n):
            for i in range(j):
                if(s[i] == s[j]):
                    if((i+1==j) or (dp[i+1][j-1])):
                        dp[i][j] = True
                        if((j-i+1) > len(output)):
                            output = s[i:j+1]
        return output