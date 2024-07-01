from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i, kid in enumerate(candies):
            if (kid + extraCandies) > (candies[i - 1]):
                result.append(True)
            else:
                result.append(False)

        return result


candies = [12, 1, 12]
extraCandies = 10

solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))
