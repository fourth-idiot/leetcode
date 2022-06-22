class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapify(minHeap)
        for num in nums:
            if(len(minHeap) < k):
                heappush(minHeap, num)
            elif(num > minHeap[0]):
                heappop(minHeap)
                heappush(minHeap, num)
            else:
                continue
        return minHeap[0]