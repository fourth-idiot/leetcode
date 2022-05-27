class Solution:
    def numberOfSteps(self, num: int) -> int:
        numSteps = 0
        while(num):
            if(num % 2): num -= 1
            else: num //= 2
            numSteps += 1
        return numSteps