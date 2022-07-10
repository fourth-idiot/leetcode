class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # For every subproblem, we can find the maximum score one can get
        # to rach the last index of the array starting from the i'th index.
        # At any index i, dp[i] becomes nums[i] + max(dp[i + 1], ..., dp[min(n - 1, i + k)].
        # To reduce its time complexity, we can the maximum value by storing dp values in a heap,
        # then we can pop out all the maximum values which around beyond k steps from i'th index.
        dp = nums.copy()
        maxHeap = [(-1 * nums[len(nums) - 1], len(nums) - 1)]
        heapify(maxHeap)
        for i in range(len(nums) - 2, -1, -1):
            while(maxHeap[0][1] > (i + k)):
                heappop(maxHeap)
            dp[i] += dp[maxHeap[0][1]]
            heappush(maxHeap, (-1 * dp[i], i))
        return dp[0]