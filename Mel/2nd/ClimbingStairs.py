def climbStairs(self, n: int) -> int:
    ans = [1] * (n + 1)
    for i in range(2, n + 1):
        ans[i] = ans[i - 1] + ans[i - 2]
    return ans[n]
