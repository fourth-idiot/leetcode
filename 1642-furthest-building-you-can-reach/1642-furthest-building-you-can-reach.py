class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        heapify(minHeap)
        previous = 0
        for i in range(1, len(heights)):
            jump = heights[i] - heights[i - 1]
            if(jump <= 0):
                continue
            elif(ladders):
                heappush(minHeap, jump)
                ladders -= 1
            elif(minHeap and (bricks >= minHeap[0])):
                heappush(minHeap, jump)
                bricks -= heappop(minHeap)
            elif(bricks >= jump):
                bricks -= jump
            else:
                return i - 1
        return len(heights) - 1