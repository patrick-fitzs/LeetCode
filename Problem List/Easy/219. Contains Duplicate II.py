from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i, value in enumerate(nums):
            if value in seen and i - seen[value] <= k:
                return True

            else:
                seen[value] = i

        return False


print(Solution().containsNearbyDuplicate([1,2,3,1],3))