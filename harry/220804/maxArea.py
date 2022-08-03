class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer, s, e = 0, 0, len(height) - 1
        while(s < e):
            answer = max(answer, min(height[s], height[e]) * (e - s))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return answer