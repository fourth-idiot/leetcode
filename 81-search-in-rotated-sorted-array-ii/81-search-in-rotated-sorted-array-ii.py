class Solution:
    def removeConsecutiveDuplicates(self, nums):
        modifiedNums = []
        for num in nums:
            if((not modifiedNums) or
               (modifiedNums[-1] != num)):
                modifiedNums.append(num)
        return modifiedNums
        
    def search(self, nums: List[int], target: int) -> bool:
        def helper(nums, start, end):
            if(start > end):
                return False
            elif(start == end):
                return nums[start] == target
            mid = (start + end) // 2
            if(nums[mid] == target):
                return True
            elif(nums[mid] < nums[end]):
                # Right side is sorted
                # So check if the target in the range of right sides extremes
                if((target > nums[mid]) and (target <= nums[end])):
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                # Left side is sorted
                # So check if the target in the range of left side extremes
                if((target >= nums[start]) and (target < nums[mid])):
                    end = mid - 1
                else:
                    start = mid + 1
            return helper(nums, start, end)
        modifiedNums = self.removeConsecutiveDuplicates(nums)
        start, end = 0, len(modifiedNums) - 1
        return helper(modifiedNums, start, end)