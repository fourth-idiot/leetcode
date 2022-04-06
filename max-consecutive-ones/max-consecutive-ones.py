class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output, currentOutput = 0, 0
        for num in nums:
            if(num == 0):
                output = max(output, currentOutput)
                currentOutput = 0
            else: currentOutput += 1
        output = max(output, currentOutput)
        return output    