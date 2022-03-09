class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prevMax = nums[0]
        maxProduct = prevMax
        prevMin = nums[0]
        for i in range(1, n):
            currentMax = max(
                nums[i],
                prevMax * nums[i],
                prevMin * nums[i]
            )
            currentMin = min(
                nums[i],
                prevMax * nums[i],
                prevMin * nums[i]
            )
            maxProduct = max(maxProduct, currentMax)
            prevMax = currentMax
            prevMin = currentMin
        return maxProduct