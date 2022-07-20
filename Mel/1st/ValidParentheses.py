class Solution:
    def isValid(self, s: str) -> bool:
        bracket_matcher = {'(':')', '[':']', '{':'}'}
        stack = []
        for x in s:
            if x in bracket_matcher:
                stack.append(x)
            elif len(stack) == 0 or bracket_matcher[stack.pop()] != x:
                return False
        return len(stack) == 0