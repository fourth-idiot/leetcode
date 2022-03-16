class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        while(i < len(pushed)):
            if(stack and (stack[-1] == popped[j])):
                stack.pop()
                j += 1
            elif(pushed[i] == popped[j]):
                i += 1
                j += 1
            else:
                stack.append(pushed[i])
                i += 1
        while(stack and (stack[-1] == popped[j])):
            stack.pop()
            j += 1
        return (len(stack) == 0)