import heapq

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        heapq.heapify(citations)
        while((citations) and (len(citations) > citations[0])):
            heapq.heappop(citations)
        return len(citations)