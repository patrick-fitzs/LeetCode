from collections import Counter
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count = Counter(candyType)
        unique_types = len(count)

        can_eat = len(candyType) // 2

        return min(unique_types, can_eat)


print(Solution().distributeCandies([1,2,3,4,5,6]))