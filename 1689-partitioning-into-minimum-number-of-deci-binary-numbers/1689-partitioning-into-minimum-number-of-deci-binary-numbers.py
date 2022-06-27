class Solution:
    def minPartitions(self, n: str) -> int:
        maxDigit = float("-inf")
        for c in n: maxDigit = max(maxDigit, int(c))
        return maxDigit