class Solution:
    def _isValidPair(self, str1, str2):
        # Checks if str1 is predecessor of str2.
        # On the first character mismatch,
        # it checks if the remaining string is equal or not.
        for i in range(len(str1)):
            if(str1[i] != str2[i]):
                return str1[i:] == str2[i+1:]
        return True
        
    def longestStrChain(self, words: List[str]) -> int:
        # Sort the list of input words in the ascending order of their length
        words.sort(key=len)
        n = len(words)
        # Initialize DP matrix with 1s as every word is a word chain of length 1
        dp = [1 for _ in range(n)]
        finalMaxLen = float("-inf")
        # For every word of length n,
        # find length of the longest word chain starting
        # with the word of length (n + 1)
        for i in range(n - 1, -1, -1):
            intermediateMaxLen = float("-inf")
            for j in range(i + 1, n):
                if(len(words[i]) == len(words[j])):
                    continue
                if(len(words[i]) != len(words[j]) - 1):
                    break
                if(self._isValidPair(words[i], words[j])):
                    intermediateMaxLen = max(intermediateMaxLen, dp[j])
            if(intermediateMaxLen != float("-inf")):
                dp[i] += intermediateMaxLen
            finalMaxLen = max(finalMaxLen, dp[i])
        return finalMaxLen