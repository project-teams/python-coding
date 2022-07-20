class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_value = 0
        stack = []
        for x in s:
            if x in stack:
                max_value = max(max_value, len(stack))
                del stack[:stack.index(x)+1]
            stack.append(x)
        return max(max_value, len(stack))