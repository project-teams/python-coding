class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        arr = [0 for _ in range(n + 1)]
        arr[1] = 1
        arr[2] = 2
        for i in range(3, n + 1):
            arr[i] = arr[i - 2] + arr[i - 1]
        return arr[n]