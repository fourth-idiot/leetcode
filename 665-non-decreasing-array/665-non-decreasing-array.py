class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def helper(nums, isInverted):
            for i in range(1, len(nums)):
                if((nums[i] < nums[i - 1]) and isInverted):
                    return False
                elif(nums[i] < nums[i - 1]):
                    nums1 = nums.copy()
                    nums1[i - 1] = nums[i]
                    nums2 = nums.copy()
                    nums2[i] = nums[i - 1]
                    return helper(nums1, True) or helper(nums2, True)
                else:
                    continue
            return True
        return helper(nums, False)