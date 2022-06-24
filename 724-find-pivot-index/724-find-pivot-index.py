class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftTotal = 0
        for i in range(len(nums)):
            if(leftTotal == ((totalSum - nums[i]) / 2)):
                return i
            else:
                leftTotal += nums[i]
        return -1