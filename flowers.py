from typing import List
from itertools import groupby


class Solution:
    def is_zeros(self, l: List[int]) -> bool:
        return sum(l) == 0

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [list(g) for k, g in groupby(flowerbed, lambda x: x > 0)]
        flowerbed = list(filter(self.is_zeros, flowerbed))
        min_sequence = min([len(f) for f in flowerbed])
        if min_sequence % n == 0:
            return True

        return False


solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], n=1))
