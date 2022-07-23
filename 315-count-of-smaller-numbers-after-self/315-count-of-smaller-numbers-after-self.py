class Solution:
    def binarySearch(self, nums, target):
        i, j = 0, len(nums) - 1
        while(i <= j):
            mid = (i + j) // 2
            if(target <= nums[mid]):
                j = mid - 1
            else:
                i = mid + 1
        return i
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0 for _ in range(n)]
        sortedNums = []
        for oldI in range(n - 1, -1, -1):
            target = nums[oldI]
            newI = self.binarySearch(sortedNums, target)
            output[oldI] = newI
            sortedNums.insert(newI, target)
            # sortedNums = sortedNums[:newI] + [target] + sortedNums[newI:]
        return output