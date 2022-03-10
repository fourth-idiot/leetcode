class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                wordLen = len(word)
                if(s[i:(i + wordLen)] == word):
                    dp[i] = dp[i] or dp[i + len(word)]
        return dp[0]