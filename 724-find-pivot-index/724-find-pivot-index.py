class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftTotal = 0
        for i in range(len(nums)):
            if((2 * leftTotal) == (total - nums[i])): return i
            else: leftTotal += nums[i]
        return -1