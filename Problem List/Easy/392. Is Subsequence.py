"""
Given two strings s and t, return true if s is a subsequence of t,
or false otherwise.

A subsequence of a string is a new string that is formed
from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1, pointer2 = 0, 0
        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                pointer1 +=1
            pointer2 += 1

        return pointer1 == len(s)


print(Solution().isSubsequence("abc", "ahbgdc"))

