class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while(i < j):
            mid = i + ((j- i) // 2)
            if(nums[mid] < nums[j]):
                j = mid
            else:
                i = mid + 1
        return nums[i]