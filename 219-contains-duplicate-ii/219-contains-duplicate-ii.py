class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i, j = 0, 0
        history = set()
        while((j <= k) and (j < n)):
            if(nums[j] in history): return True
            else: history.add(nums[j])
            j += 1
        if(j == n): return False
        while(j < n):
            history.remove(nums[i])
            i += 1
            if(nums[j] in history): return True
            else: history.add(nums[j])
            j += 1
        return False