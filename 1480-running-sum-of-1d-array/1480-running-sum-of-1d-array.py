class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Instead of creating a new array of cumulative sums,
        # we can replace each element with the sum of
        # previous cumulative sum and the element itself.
        # It will represent the cumulative sum till that element.
        # Time complexity: O(n)
        # Space complexity: O(1)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums