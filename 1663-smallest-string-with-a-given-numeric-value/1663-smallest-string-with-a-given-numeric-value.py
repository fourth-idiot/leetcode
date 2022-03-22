class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        allChars = "abcdefghijklmnopqrstuvwxyz"
        output = []
        for i in range(n):
            idx = max(k-26*(n-i-1), 1)
            output.append(allChars[idx-1])
            k -= (idx)
        return "".join(output)