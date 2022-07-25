class Solution:
    def binarySearchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            if(target <= nums[mid]):
                right = mid
            else:
                left = mid + 1
        return left if (nums[left] == target) else -1
        
    def binarySearchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = ((left + right) // 2) + 1
            if(target < nums[mid]):
                right = mid - 1
            else:
                left = mid
        return left if (nums[left] == target) else -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(not nums):
            return [-1, -1]
        return [self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)]