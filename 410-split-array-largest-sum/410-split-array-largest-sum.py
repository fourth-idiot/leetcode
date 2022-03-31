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
        if(nums[0] > target):
            return False
        s = nums[0]
        count = 1
        for num in nums[1:]:
            if(num > target):
                return False
            s += num
            if(s > target):
                count += 1
                s = num
        return (count <= m)
    
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