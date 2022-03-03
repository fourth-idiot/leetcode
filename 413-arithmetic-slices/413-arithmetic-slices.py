class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return 0
        output = 0
        diff = nums[1] - nums[0]
        count = 2
        for i in range(2, len(nums)):
            currentDiff = nums[i] - nums[i-1]
            if(currentDiff == diff):
                count += 1
            else:
                # [Core logic to calculate the number of subarrays with same difference between consecutive elements]
                # Find total number of subarrays using following formula
                # If there are n elements in a subarray, there will be:
                # I. 1 subarray of length n
                # II. 2 subarray of length (n-1)
                # III. 3 subarrays of length (n-2), and so on.
                # IV. Finally, there will be (n-3) subarrays of length 3
                # Hence, it forms an Arithmetic progression: 1, 2, 3, ..., (n-3)
                # Its sum is equal to ((n - 1) * (n - 2)) / 2
                if(count >= 3):
                    output += (((count - 1) * (count - 2)) // 2)
                diff = currentDiff
                count = 2
        if(count >= 3):
            output += (((count - 1) * (count - 2)) // 2)
        return output