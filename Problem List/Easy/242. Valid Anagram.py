"""
https://leetcode.com/problems/valid-anagram/

we could sort both and compare. This is O(n log n) for the sort function.
OR
we use counter for O(n)
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # return s == t

        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t

