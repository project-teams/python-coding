from typing import List


class Solution338:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            binary = list(bin(i))
            result.append(binary.count('1'))

        return result
