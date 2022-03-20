class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        commons = set((tops[0], bottoms[0]))
        for i in range(1, n):
            commons = commons & set((tops[i], bottoms[i]))
        if(len(commons) == 0):
            return -1
        output = float("inf")
        for val in commons:
            # Make top/bottom equal to the val
            top_count, bottom_count = 0, 0
            for i in range(n):
                if(tops[i] != val):
                    top_count += 1
                if(bottoms[i] != val):
                    bottom_count += 1
            output = min(output, top_count, bottom_count)
        return output
                    