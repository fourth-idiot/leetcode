class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if(len(nums1) < len(nums2)):
            counter1 = {}
            for num in nums1:
                counter1[num] = counter1.get(num, 0) + 1
            output = []
            for num in nums2:
                count = counter1.get(num, 0)
                if(count > 0):
                    output.append(num)
                    counter1[num] -= 1
        else:
            counter2 = {}
            for num in nums2:
                counter2[num] = counter2.get(num, 0) + 1
            output = []
            for num in nums1:
                count = counter2.get(num, 0)
                if(count > 0):
                    output.append(num)
                    counter2[num] -= 1
        return output