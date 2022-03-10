class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        maxLen = float("-inf")
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if(nums[j] > nums[i]):
                    dp[i] = max(dp[i], 1 + dp[j])
            if(dp[i] > maxLen):
                maxLen = dp[i]
        return maxLen