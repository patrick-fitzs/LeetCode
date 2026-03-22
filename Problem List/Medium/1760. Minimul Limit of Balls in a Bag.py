"""
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/

we have an array [9] and want to split it maxOperations times
So it would make sense for us to halve the max num each time,

"""
import math
class Solution:
    def minimumSize(self, nums, maxOperations):
        left, right = 1, max(nums)

        while left < right:
            middle = (left + right) // 2

            operations = 0
            for n in nums:
                operations += (n-1) // middle

            if operations <= maxOperations:
                right = middle
            else:
                left = middle + 1
        return left


print(Solution().minimumSize([9], 2))
