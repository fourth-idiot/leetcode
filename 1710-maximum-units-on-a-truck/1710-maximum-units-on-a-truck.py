class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # boxTypes.sort(key=lambda x: -x[1])
        # totalUnits = 0
        # remainingTruckSize = truckSize
        # for i in range(len(boxTypes)):
        #     numBoxes = min(boxTypes[i][0], remainingTruckSize)
        #     remainingTruckSize -= numBoxes
        #     totalUnits += (numBoxes * boxTypes[i][1])
        #     if(remainingTruckSize == 0):
        #         break
        # return totalUnits
        
        minHeap = []
        heapify(minHeap)
        for numBoxes, numUnitsPerBox in boxTypes:
            for _ in range(numBoxes):
                heappush(minHeap, numUnitsPerBox)
                if(len(minHeap) > truckSize):
                    heappop(minHeap)
        return sum(minHeap)