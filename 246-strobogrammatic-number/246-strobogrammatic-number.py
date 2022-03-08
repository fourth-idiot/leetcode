class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # d = {
        #     "0": "0",
        #     "1": "1",
        #     "6": "9",
        #     "8": "8",
        #     "9": "6"
        # }
        # i, j = 0, len(num)-1
        # while(i <= j):
        #     if(num[i] not in d):
        #         return False
        #     elif(d[num[i]] != num[j]):
        #         return False
        #     else:
        #         i += 1
        #         j -= 1
        # return True
        
        dp = {}
        def isStrobogrammatic1(num: str) -> bool:
            d = {
                "0": "0",
                "1": "1",
                "6": "9",
                "8": "8",
                "9": "6"
            }
            if(num in dp):
                return dp[num]
            elif(num == ""):
                dp[num] = True
                return True
            elif((num[0] not in d) or (d[num[0]] != num[-1])):
                dp[num] = False
                return False
            else:
                subStringOutput = isStrobogrammatic1(num[1:-1])
                dp[num[1:-1]] = subStringOutput
                return subStringOutput
        return isStrobogrammatic1(num)
                