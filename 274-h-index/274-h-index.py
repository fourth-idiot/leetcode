import heapq

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        minHeap = citations.copy()
        heapq.heapify(minHeap)
        hIndex = 0
        while((minHeap) and (len(minHeap) > minHeap[0])):
            hIndex = heapq.heappop(minHeap)
        return len(minHeap)