"""
https://leetcode.com/problems/first-unique-character-in-a-string/

We have a string s and need to find the first non repeating character, else return -1

create a map with counters, iterate and return the index where counts[ch]==1
"""


import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)

        for index, chr in enumerate(s):
            if counter[chr] == 1:
                return index

        return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
