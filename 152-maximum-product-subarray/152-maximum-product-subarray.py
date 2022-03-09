class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prevMax = nums[0]
        maxProduct = prevMax
        prevMin = nums[0]
        for i in range(1, n):
            currentMin, _, currentMax = sorted([nums[i], prevMin * nums[i], prevMax * nums[i]])
            maxProduct = max(maxProduct, currentMax)
            prevMax = currentMax
            prevMin = currentMin
        return maxProduct