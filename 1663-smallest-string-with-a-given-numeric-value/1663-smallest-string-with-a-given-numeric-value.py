class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        allChars = "abcdefghijklmnopqrstuvwxyz"
        output = []
        for i in range(n):
            charIdx = max(k-26*(n-i-1), 1)
            output.append(allChars[charIdx - 1])
            k -= charIdx
        return "".join(output)