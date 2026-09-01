from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1) # create a counter of each num so we can decrement as we go

        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result

#print(Solution().intersect([4,9,5],[9,4,9,8,4]))
print(Solution().intersect([1,2,2,1],[2,2]))