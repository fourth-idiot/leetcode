class Solution:
    def binarySearch(self, nums, target):
        start, end = 0, len(nums) - 1
        while(start < end):
            mid = (start + end) // 2
            if(target <= nums[mid]): end = mid
            else: start = mid + 1
        return nums[start] == target
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            contains = self.binarySearch(matrix[i], target)
            if(contains):
                return True
        return False