class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the index where which will be replaced by next possible number
        if(len(nums) < 2): return nums
        p1 = len(nums) - 2
        while((p1 >= 0) and (nums[p1] >= nums[p1 + 1])):
            p1 -= 1
        # Find the next possible number
        if(p1 >= 0):
            p2 = len(nums) - 1
            while(nums[p2] <= nums[p1]): p2 -= 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
        # Reverse the remaining list
        p1 += 1
        p2 = len(nums) - 1
        while(p1 < p2):
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1
        return