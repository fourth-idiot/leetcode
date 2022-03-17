class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for c in s:
            if(c == "("):
                stack.append(score)
                score = 0
            else:
                v = stack.pop()
                score = v + max(score * 2, 1)
        return score