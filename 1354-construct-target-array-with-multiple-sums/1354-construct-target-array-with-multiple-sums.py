class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if(len(target) == 1):
            return target[0] == 1
        total = sum(target)
        maxHeap = [-val for val in target]
        heapify(maxHeap)
        while(maxHeap[0] != -1):
            maxVal = -heappop(maxHeap)
            remainingTotal = total - maxVal
            if remainingTotal == 1:
                return True
            remainingVal = maxVal % remainingTotal
            if((remainingVal == 0) or (remainingVal == maxVal)):
                return False
            heappush(maxHeap, -remainingVal)
            total -= (maxVal - remainingVal)
        return True