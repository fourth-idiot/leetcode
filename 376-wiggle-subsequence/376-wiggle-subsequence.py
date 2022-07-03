class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # [1, 4, 4, 1, 2, 1]
        # [1, 5, 3, 3, 1, 1]
        n = len(nums)
        dp = [[1 for _ in range(n)] for _ in range(2)]
        for i in range(n - 2, -1, -1):
            # Find the positive subsequence starting from i'th index
            maxVal = 0
            for j in range(i + 1, n):
                if(nums[j] > nums[i]):
                    maxVal = max(maxVal, dp[1][j])
            dp[0][i] += maxVal
            # Find the negative subsequence starting from i'th index
            maxVal = 0
            for j in range(i + 1, n):
                if(nums[j] < nums[i]):
                    maxVal = max(maxVal, dp[0][j])
            dp[1][i] += maxVal
        return max(dp[0][0], dp[1][0])