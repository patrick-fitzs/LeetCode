'''
Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:

Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
Return the maximum possible value of x.

Example 1:

Input: num = 4, t = 1

Output: 6

Example 2:

Input: num = 3, t = 2

Output: 7
'''

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t