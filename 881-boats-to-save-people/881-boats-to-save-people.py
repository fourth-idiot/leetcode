class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # # Approach 1
        # people.sort()
        # n = len(people)
        # visited = [False for _ in range(n)]
        # count = 0
        # p1 = n - 1
        # while(p1 >= 0):
        #     if(not visited[p1]):
        #         visited[p1] = True
        #         remainingLimit = limit - people[p1]
        #         p2 = p1 - 1
        #         while((p2 >= 0) and
        #               ((people[p2] > remainingLimit) or (visited[p2]))):
        #             p2 -= 1
        #         if(p2 >= 0): visited[p2] = True
        #         count += 1
        #     p1 -= 1
        # return count
        
        
        # # Approach 2
        # def twoSum(counter, target):
        #     count = 0
        #     for weight in weights:
        #         if(counter[weight] > 0):
        #             remainingTarget = target - weight
        #             if(remainingTarget == 0):
        #                 count += counter[target]
        #                 counter[target] = 0
        #             elif(remainingTarget == weight):
        #                 count += (counter[weight] // 2)
        #                 counter[weight] %= 2
        #             elif((remainingTarget in counter) and (counter[remainingTarget] > 0)):
        #                 temp = min(counter[weight], counter[remainingTarget])
        #                 count += temp
        #                 counter[weight] -= temp
        #                 counter[remainingTarget] -= temp
        #     return count
        # counter = {}
        # weights = set()
        # for weight in people:
        #     counter[weight] = counter.get(weight, 0) + 1
        #     weights.add(weight)
        # weights = sorted(list(weights), reverse=True)
        # output = 0
        # for target in range(limit, 0, -1):
        #     currentOutput = twoSum(counter, target)
        #     output += currentOutput
        # return output
        
        # Approach 3
        people.sort()
        i, j = 0, len(people) - 1
        count = 0
        while(i <= j):
            if((people[i] + people[j]) <= limit):
                i += 1
                j -= 1
                count += 1
            else:
                j -= 1
                count += 1
        return count