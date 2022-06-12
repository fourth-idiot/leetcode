class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        val, maxVal = 0, 0
        history = set()
        i, j = 0, 0
        while(j < len(nums)):
            if(nums[j] in history):
                maxVal = max(val, maxVal)
                while(nums[i] != nums[j]):
                    history.remove(nums[i])
                    val -= nums[i]
                    i += 1
                i += 1
            else:
                history.add(nums[j])
                val += nums[j]
            j += 1
        return max(val, maxVal)