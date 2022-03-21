import heapq

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        minHeap = citations.copy()
        heapq.heapify(minHeap)
        while((minHeap) and (len(minHeap) > minHeap[0])):
            heapq.heappop(minHeap)
        return len(minHeap)