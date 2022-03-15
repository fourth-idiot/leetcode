class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        totalStack = []
        pStack = []
        for c in s:
            if(c.isalpha()):
                totalStack.append(c)
            elif(c == "("):
                pStack.append(c)
                totalStack.append(c)
            elif(c == ")"):
                if(pStack):
                    lastP = pStack[-1]
                    if(lastP == "("):
                        pStack.pop()
                        totalStack.append(c)
        updatedTotalStack = []
        pStack = []
        for c in totalStack[::-1]:
            if(c.isalpha()):
                updatedTotalStack.append(c)
            elif(c == ")"):
                pStack.append(c)
                updatedTotalStack.append(c)
            elif(c == "("):
                if(pStack):
                    lastP = pStack[-1]
                    if(lastP == ")"):
                        pStack.pop()
                        updatedTotalStack.append(c)
        return "".join(updatedTotalStack[::-1])