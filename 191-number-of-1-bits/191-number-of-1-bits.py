class Solution:
    def hammingWeight(self, n: int) -> int:
        # When we subtract 1 from the binary representation of an integer,
        # it changes the rightmost string of 0s to 1s,
        # changes the least significant 1 to 0,
        # and keeps everything else the same.
        # As a result, n replaced with the bitwise AND of n with n - 1
        # differs from the previous n with the least significant 1 changed to 0.
        # If we repeat these steps until n becomes 0,
        # then the number of steps is equal to the number of 1s in the given n.
        s = 0
        while(n):
            s += 1
            n &= (n - 1)
        return s