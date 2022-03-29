class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # Approach 1
        # nums.sort()
        # lastNum = nums[0]
        # for num in nums[1:]:
        #     if(num == lastNum):
        #         return num
        #     lastNum = num
        
        # # Approach 2
        # seen = set()
        # for num in nums:
        #     if(num in seen):
        #         return num
        #     seen.add(num)
        
        # Approach 3
        for num in nums:
            absNum = abs(num)
            if(nums[absNum] < 0):
                return absNum
            else:
                nums[absNum] *= -1