class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        while(i < len(pushed)):
            if(stack and (stack[-1] == popped[0])):
                stack.pop()
                popped.pop(0)
            elif(pushed[i] == popped[0]):
                popped.pop(0)
                i += 1
            else:
                stack.append(pushed[i])
                i += 1
        while(stack and (stack[-1] == popped[0])):
            stack.pop()
            popped.pop(0)
        return (len(stack) == 0)