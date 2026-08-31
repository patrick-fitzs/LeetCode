"""
https://leetcode.com/problems/first-unique-character-in-a-string/

We have a string s and need to find the first non repeating character, else return -1

create a map with counters, iterate and return the index where counts[ch]==1
"""

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # start with a hash map with counters
        counts = collections.Counter(s)

        # iterate over each index(letter) of s with its letter(value)
        for index, value in enumerate(s):
            # if the counts value of the current value is 1, return it as its the first unique
            if counts[value] == 1:
                return index

        return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
