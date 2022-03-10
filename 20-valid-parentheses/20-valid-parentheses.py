class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if((c == "(") or (c == "[") or (c == "{")):
                stack.append(c)
            elif(not stack):
                return False
            else:
                lastParentheses = stack.pop()
                if(((c == ")") and (lastParentheses != "(")) or
                   ((c == "]") and (lastParentheses != "[")) or
                   ((c == "}") and (lastParentheses != "{"))):
                    return False
        return len(stack) == 0