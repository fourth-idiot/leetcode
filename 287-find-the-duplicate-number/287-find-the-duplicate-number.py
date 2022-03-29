class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        lastNum = nums[0]
        for num in nums[1:]:
            if(num == lastNum):
                return num
            lastNum = num