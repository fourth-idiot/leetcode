class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while(i < j):
            # Find the sorted half
            mid = i + ((j - i) // 2)
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < nums[j]):
                # Right side is sorted
                if((target > nums[mid]) and (target <= nums[j])):
                    # Target element is in the right side
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                # Left side is sorted
                if((target >= nums[i]) and (target < nums[mid])):
                    j = mid - 1
                else:
                    i = mid + 1
        if(nums[i] == target):
            return i
        else:
            return -1