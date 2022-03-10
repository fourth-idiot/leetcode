class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[-1] = True
        for i in range(n - 1, -1, -1):
            if((i + nums[i]) >= (n - 1)):
                dp[i] = True
                n = i + 1
        return dp[0]