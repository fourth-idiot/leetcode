class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = nums.copy()
        maxHeap = [(-1 * nums[len(nums) - 1], len(nums) - 1)]
        heapify(maxHeap)
        for i in range(len(nums) - 2, -1, -1):
            while(maxHeap[0][1] > (i + k)):
                heappop(maxHeap)
            dp[i] += dp[maxHeap[0][1]]
            heappush(maxHeap, (-1 * dp[i], i))
        return dp[0]