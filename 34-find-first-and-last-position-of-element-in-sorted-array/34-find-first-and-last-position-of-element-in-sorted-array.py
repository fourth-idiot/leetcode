class Solution:
    def binarySearchLeft(self, nums, target):
        if(not nums):
            return -1
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            if(target <= nums[mid]):
                right = mid
            else:
                left = mid + 1
        if(nums[left] == target):
            return left
        else:
            return -1
        
    def binarySearchRight(self, nums, target):
        if(not nums):
            return -1
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = ((left + right) // 2) + 1
            if(target < nums[mid]):
                right = mid - 1
            else:
                left = mid
        if(nums[left] == target):
            return left
        else:
            return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)]