from functools import cmp_to_key

class Solution:
    def compare(self, record1, record2):
        # Compare two records on the basis of Manhattan function
        if(record1[0] < record2[0]):
            return -1
        elif(record2[0] < record1[0]):
            return 1
        else:
            # If Manhattan distance is same,
            # compare two records on the basis of worker index
            if(record1[1] < record2[1]):
                return -1
            elif(record2[1] < record1[1]):
                return 1
            else:
                # If both Manhattan distance and worker index is same,
                # compare two records on the basis of bike index
                if(record1[2] < record2[2]):
                    return -1
                elif(record2[2] < record1[2]):
                    return 1
                else:
                    return 0
        
    def getManhattenDist(self, p1, p2):
        return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
        
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        allOptions = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                allOptions.append([self.getManhattenDist(workers[i], bikes[j]), i, j])
        allOptions.sort()
        # allOptions.sort(key=cmp_to_key(self.compare))
        count = 0
        assignedWorkers = [-1 for _ in range(len(workers))]
        assignedBikes = [False for _ in range(len(bikes))]
        for option in allOptions:
            dist, worker, bike = option
            if((assignedWorkers[worker] == -1) and (not assignedBikes[bike])):
                assignedWorkers[worker] = bike
                assignedBikes[bike] = True
                count += 1
            if(count == len(workers)):
                break
        return assignedWorkers