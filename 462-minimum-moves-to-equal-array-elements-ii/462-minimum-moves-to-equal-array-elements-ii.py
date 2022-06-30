class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        j = len(nums) - 1
        mid, remaining = divmod(j, 2)
        if(remaining): target = (nums[mid] + nums[mid + 1]) // 2
        else: target = nums[mid]
        output = 0
        for num in nums:
            output += abs(target - num)
        return output