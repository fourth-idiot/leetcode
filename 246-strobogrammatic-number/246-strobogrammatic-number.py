class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        i, j = 0, len(num)-1
        while(i <= j):
            if(num[i] not in d):
                return False
            elif(d[num[i]] != num[j]):
                return False
            else:
                i += 1
                j -= 1
        return True
                