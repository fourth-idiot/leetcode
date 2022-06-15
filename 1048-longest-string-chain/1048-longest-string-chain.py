class Solution:
    def isValidPair(self, str1, str2):
        for i in range(len(str1)):
            if(str1[i] != str2[i]):
                return str1[i:] == str2[(i + 1):]
        return True
        
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda s: len(s))
        dp = [1 for _ in range(n)]
        for i in range(n, -1, -1):
            maxVal = float("-inf")
            for j in range(i + 1, n):
                if(len(words[i]) == len(words[j])):
                    continue
                elif(len(words[i]) != len(words[j]) - 1):
                    break
                elif(self.isValidPair(words[i], words[j])):
                    maxVal = max(maxVal, dp[j])
            if(maxVal != float("-inf")):
                dp[i] += maxVal
        return max(dp)