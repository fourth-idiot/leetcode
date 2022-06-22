class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapify(minHeap)
        for num in nums:
            if((len(minHeap) >= k) and (num > minHeap[0])):
                heappop(minHeap)
            if(len(minHeap) < k):
                heappush(minHeap, num)
        return minHeap[0]