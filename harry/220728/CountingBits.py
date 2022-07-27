class Solution:
    def countBits(self, n: int) -> List[int]:
        return [sum(map(int, list(format(i, 'b')))) for i in range(n + 1)]