"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in range 1 - len(str1) - len(str2) + 1 because of indexing
        for i in range(len(haystack) - len(needle) + 1):
            # of i - len(str2) == str2
            if haystack[i:i + len(needle)] == needle:
                # returns the starting index i where this string starts
                return i

        return -1

print()
print(Solution().strStr("sadbutsad", "sad"))
