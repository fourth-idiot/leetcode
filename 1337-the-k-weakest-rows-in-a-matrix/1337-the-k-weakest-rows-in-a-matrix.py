import heapq

class Row:
    def __init__(self, idx, row):
        self.idx = idx
        self.row = row
        self.numSoldiers = sum(self.row)
        
    def __lt__(self, nxt):
        if(self.numSoldiers == nxt.numSoldiers):
            return self.idx > nxt.idx
        return self.numSoldiers > nxt.numSoldiers

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        maxHeap = []
        heapq.heapify(maxHeap)
        # Takes O(KLogN + N) time to add elements to the heap
        for i, row in enumerate(mat):
            rowItem = Row(i, row)
            if((len(maxHeap) == k) and (rowItem > maxHeap[0])):
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, rowItem)
            elif(len(maxHeap) < k):
                heapq.heappush(maxHeap, rowItem)
        output = []
        # Takes O(K) time to get indices of K weakest rows
        while(len(maxHeap) > 0):
            rowItem = heapq.heappop(maxHeap)
            output.append(rowItem.idx)
        return output[::-1]