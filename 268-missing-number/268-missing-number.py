class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        return int(n / 2 * (n - 1)) - sum(nums)