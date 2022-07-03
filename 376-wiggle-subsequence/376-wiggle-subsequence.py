class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Before solving this problem, we will define two things:
        # 1. Positive subsequence: Subsequence in which difference between
        # the first two elements is +ve. For example: [1, 2]
        # 2. Negative subsequence: Subsequence in which difference between
        # the first two elements is -ve. For example: [2, 1]
        
        # We can define this problem as a dynamic programming problem as following:
        # Firstly, we create a 2D array of dimension 2 * len(nums), having default value of each element as 1.
        # First row represents the maximum length of +ve subsequence starting from i'th index.
        # This value can be calculated as following:
        # We will loop over all values starting from (i + 1)'th index to find all values GREATER than nums[i].
        # Out of all those values, we need value with the longest negative subsequence.
        # Hence, dp[0][i] += max([dp[1][j] for j in range(i + 1, len(nums)) if (nums[j] > nums[i])])
        # Similarly, dp[1][i] += max([dp[0][j] for j in range(i + 1, len(nums)) if (nums[j] < nums[i])])
        
        # Example:
        # For [1, 7, 4, 9, 2, 5]:
        # DP matrix of dimensions 2 * 6 can be initialized as following:
        # dp = [[1, 1, 1, 1, 1, 1],
        #       [1, 1, 1, 1, 1, 1]]
        # Now we can calculate DP matrix in backward direction as following:
        # For i = 4:
        # dp = [[1, 1, 1, 1, 1 + max(1), 1],
        #       [1, 1, 1, 1, 1, 1]]
        # For i = 3:
        # dp = [[1, 1, 1, 1, 2, 1],
        #       [1, 1, 1, 1 + max(2, 1), 1, 1]]
        # For i = 2:
        # dp = [[1, 1, 1 + max(3, 1), 1, 2, 1],
        #       [1, 1, 1 + max(2), 3, 1, 1]]
        # For i = 1:
        # dp = [[1, 1 + max(3), 4, 1, 2, 1],
        #       [1, 1 + max(4, 2, 1), 3, 3, 1, 1]]
        # For i = 0:
        # dp = [[1 + max(5, 3, 3, 1, 1), 4, 4, 1, 2, 1],
        #       [1, 5, 3, 3, 1, 1]]
        # Now, dp matrix becomes as following:
        # dp = [[6, 4, 4, 1, 2, 1],
        #       [1, 5, 3, 3, 1, 1]]
        # Finally maximum value out of +ve and -ve subsequence starting from 0'th index
        # will be our answer.
        
        n = len(nums)
        dp = [[1 for _ in range(n)] for _ in range(2)]
        for i in range(n - 2, -1, -1):
            # Find the longest negative subsequence starting from (i + 1)'th index
            maxVal = 0
            for j in range(i + 1, n):
                if(nums[j] > nums[i]):
                    maxVal = max(maxVal, dp[1][j])
            dp[0][i] += maxVal
            # Find the longest positive subsequence starting from (i + 1)'th index
            maxVal = 0
            for j in range(i + 1, n):
                if(nums[j] < nums[i]):
                    maxVal = max(maxVal, dp[0][j])
            dp[1][i] += maxVal
        return max(dp[0][0], dp[1][0])