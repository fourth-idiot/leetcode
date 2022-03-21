class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i in range(n):
            if(not ((n-i) > citations[i])):
                return (n-i)
        return 0