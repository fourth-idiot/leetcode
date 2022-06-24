class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftTotal = 0
        for i in range(len(nums)):
            if((2 * leftTotal) == (totalSum - nums[i])): return i
            else: leftTotal += nums[i]
        return -1