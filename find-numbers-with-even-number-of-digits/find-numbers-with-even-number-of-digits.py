import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            numDigits = math.floor(math.log10(num)) + 1
            if(numDigits % 2 == 0): count += 1
        return count