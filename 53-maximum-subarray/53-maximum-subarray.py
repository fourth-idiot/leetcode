class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = currentSum
        for num in nums[1:]:
            currentSum = max(currentSum + num, num)
            maxSum = max(currentSum, maxSum)
        return maxSum