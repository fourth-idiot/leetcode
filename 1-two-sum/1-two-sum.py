class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if(diff in numIndexMap):
                return [numIndexMap[diff], i]
            else:
                numIndexMap[num] = i
        return None