class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        minDp = [0 for _ in range(n)]
        minDp[0] = nums[0]
        maxDp = [0 for _ in range(n)]
        maxDp[0] = nums[0]
        for i in range(1, n):
            minDp[i] = min(
                nums[i],
                minDp[i-1] * nums[i],
                maxDp[i-1] * nums[i]
            )
            maxDp[i] = max(
                nums[i],
                minDp[i-1] * nums[i],
                maxDp[i-1] * nums[i]
            )
        return max(maxDp)
            