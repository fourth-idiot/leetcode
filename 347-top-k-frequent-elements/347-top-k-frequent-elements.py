import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        minHeap = []
        heapq.heapify(minHeap)
        for num, freq in counter.items():
            if((len(minHeap) == k) and (freq > minHeap[0][0])):
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (freq, num))
            elif(len(minHeap) < k):
                heapq.heappush(minHeap, (freq, num))
        output = [val[1] for val in minHeap]
        return output