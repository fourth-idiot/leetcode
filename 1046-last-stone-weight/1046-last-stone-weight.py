import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for stone in stones:
            heapq.heappush(maxHeap, -1 * stone)
        while(len(maxHeap) > 1):
            heaviestStone = -1 * heapq.heappop(maxHeap)
            heavierStone = -1 * heapq.heappop(maxHeap)
            if(heaviestStone != heavierStone):
                heapq.heappush(maxHeap, -1 * (heaviestStone - heavierStone))
        if(len(maxHeap) == 0):
            return 0
        else:
            return -1 * maxHeap[0]