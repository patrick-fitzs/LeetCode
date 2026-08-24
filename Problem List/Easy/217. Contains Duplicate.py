"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct
"""

# Fairly easy hash set following 1. Two Sum hash map option

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # create a set with seen so we avoid duplicates
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)

        else:
            return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))