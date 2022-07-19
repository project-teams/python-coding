"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order. 
"""
class Solution20:
    def isValid(self, s: str) -> bool:
        dict = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        #홀수이면 무조건 False
        if(len(s) % 2 != 0):
            return False

        for str in s:
            if(str in dict.keys()):
                stack.append(str)
            else:
                if(stack == []):
                    return False
                
                pop = stack.pop()
                if str!= dict[pop]:
                    return False
        
        return stack == []

