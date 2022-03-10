class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxL = 0
        for num in nums:
            if((num - 1) not in numsSet):
                l = 0
                start = num
                while(start in numsSet):
                    l += 1
                    start += 1
                maxL = max(maxL, l)
        return maxL