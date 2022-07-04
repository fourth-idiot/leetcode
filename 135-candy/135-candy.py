class Solution:
    def candy(self, ratings: List[int]) -> int:
        minHeap = [(val, idx) for (idx, val) in enumerate(ratings)]
        heapify(minHeap)
        output = [1 for _ in range(len(minHeap))]
        while(minHeap):
            val, idx = heappop(minHeap)
            if(((idx - 1) >= 0) and
               ((ratings[idx - 1]) > ratings[idx])):
                output[idx - 1] = max(output[idx - 1], output[idx] + 1)
            if(((idx + 1) < len(ratings)) and
               ((ratings[idx + 1]) > ratings[idx])):
                output[idx + 1] = max(output[idx + 1], output[idx] + 1)
        return sum(output)