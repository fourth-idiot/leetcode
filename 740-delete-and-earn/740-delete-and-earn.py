class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        else:
            nums.sort()
            n = len(nums)
            counter = {}
            for num in nums:
                counter[num] = counter.get(num, 0) + 1
            dp = [0] * (n + 1)
            for currentNumIdx in range(n - 1, -1, -1):
                nextNumIdx = currentNumIdx + 1
                while(nextNumIdx < n):
                    if(nums[nextNumIdx] == (nums[currentNumIdx] + 1)):
                        break
                    else:
                        nextNumIdx += 1
                nextToNextNumIdx = currentNumIdx + 1
                while(nextToNextNumIdx < n):
                    if((nums[nextToNextNumIdx] >= nums[currentNumIdx] + 2)):
                        break
                    else:
                        nextToNextNumIdx += 1
                dp[currentNumIdx] = max(
                    (counter[nums[currentNumIdx]] * nums[currentNumIdx]) + dp[nextToNextNumIdx],
                    dp[nextNumIdx]
                )
        return dp[0]