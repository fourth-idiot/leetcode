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
        # For every nums[i], since we need number of smaller elements to the right,
        # we will start iterating from end of the list in reverse order.
        # Using binary search, We will find its position `i` in the sorted list of numbers to its right. `i` will also be the number of smaller elements than that number.
        # Hence, we will update that value in the output and add number to that index in the sorted list.
        # Finally we will return the list
        n = len(nums)
        output = [0 for _ in range(n)]
        sortedNums = []
        for oldI in range(n - 1, -1, -1):
            target = nums[oldI]
            newI = self.binarySearch(sortedNums, target)
            output[oldI] = newI
            sortedNums.insert(newI, target)
        return output