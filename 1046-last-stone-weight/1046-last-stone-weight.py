class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapify(maxHeap)
        for stone in stones:
            heappush(maxHeap, -1 * stone)
        while(len(maxHeap) > 1):
            heaviestStone = -1 * heappop(maxHeap)
            heavierStone = -1 * heappop(maxHeap)
            if(heaviestStone != heavierStone):
                heappush(maxHeap, -1 * (heaviestStone - heavierStone))
        return -1 * maxHeap[0] if maxHeap else 0