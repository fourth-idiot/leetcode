class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Since each child must have at least one candy,
        # we can initialize an unit array of length `len(ratings)`.
        
        # If we store all the elements and their indices in an heap,
        # then we can GREEDILY pop the element with the lowest value.
        # Now, we can find its neighbouring elements having higher rating.
        # If the number of candies assigned to the child with higher ratings
        # is less than or equal to its neighbour, then we can update its value.
        # This way we will get an array of the final assignments,
        # and sum of that array will be our answer.
        
        minHeap = [(val, idx) for (idx, val) in enumerate(ratings)]
        heapify(minHeap)
        output = [1 for _ in range(len(minHeap))]
        while(minHeap):
            val, idx = heappop(minHeap)
            if(((idx - 1) >= 0) and
               ((ratings[idx - 1]) > ratings[idx])):
                output[idx - 1] = max(output[idx - 1], output[idx] + 1)
            if(((idx + 1) < len(ratings)) and
               ((ratings[idx + 1]) > ratings[idx])):
                output[idx + 1] = max(output[idx + 1], output[idx] + 1)
        return sum(output)