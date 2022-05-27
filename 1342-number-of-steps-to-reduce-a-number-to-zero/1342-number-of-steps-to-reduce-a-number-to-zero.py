class Solution:
    def numberOfSteps(self, num: int) -> int:
        # # Approach 1: Using simulation
        # numSteps = 0
        # while(num):
        #     if(num % 2): num -= 1
        #     else: num //= 2
        #     numSteps += 1
        # return numSteps
    
        # Approach 2: Using binary representation of the number
        # Let's say we need to reduce 210 to 0
        # (Integer) = (Binary representation)
        # 210 = 11010010    // If the least significant bit is zero i.e. current number is even,
        #                   // it takes SINGLE step to reduce the number of bits
        #                   // (by which the number is represented) by 1
        # 105 = 1101001     // If the least significant bit is one i.e. current number is odd,
        #                   // it takes TWO steps to reduce the number of bits
        #                   // (by which the number is represented) by 1
        # 104 = 1101000
        # 72 = 110100
        # Hence, we can calculate the total number of steps from the binary representation in the following manner:
        # i. Initialize total number of steps (numSteps) to zero
        # ii. If the bit value is zero, increment numSteps by 1
        # iii. Else, increment numSteps by 2
        numSteps = 0
        binaryNum = format(num, "b")
        for digit in binaryNum:
            if(digit == "0"): numSteps += 1
            else: numSteps += 2
        return numSteps - 1