class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # iterate over haystack input
        for i in range(len(haystack)):
            # compare substrings
            # compare a substring from haystack of equal length to that of needle
            if haystack[i:i + len(needle)] == needle:
                return i
        else:
            return -1

