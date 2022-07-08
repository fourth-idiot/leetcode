class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                val = (s[i:(j + 1)] in wordDict) and dp[j + 1]
                if(val):
                    dp[i] = True
                    break
        return dp[0]