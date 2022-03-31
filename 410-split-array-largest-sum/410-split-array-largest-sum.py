# low = 1
# high = 32

# mid 16

# k = 3

# low = mid + 1 = 17
# high = 32
# mid = 49 / 2 = 24
# maxsum = 24

# high = mid - 1 = 23
# low = 17
# mid = 20
# maxSum = 20

# high = 19
# low = 17
# mid = 18
# maxSum = 18

# high = 18
# mid = 17

# low = 18

class Solution:
    def isPartitioningPossible(self, nums, target, m):
        subArraySum, subArrayCount = 0, 0
        i = 0
        while(i < len(nums)):
            if(nums[i] > target):
                return False
            subArraySum += nums[i]
            if(subArraySum > target):
                subArraySum = 0
                subArrayCount += 1
            else:
                i += 1
        if(subArraySum != 0):
            subArrayCount += 1
        return (subArrayCount <= m)
    
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = 1, sum(nums)
        maxSum = sum(nums)
        while(low <= high):
            mid = (low + high) // 2
            if(self.isPartitioningPossible(nums, mid, m)):
                maxSum = mid
                high = mid - 1
            else:
                low = mid + 1
        return maxSum