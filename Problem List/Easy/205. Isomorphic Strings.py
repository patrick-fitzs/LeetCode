"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters.
No two characters may map to the same character,
but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs
to be mapped to both 'a' and 'r'.
"""

# how we can do this is to create two maps
# add each letter one by one which adds a tally in the form of a value
# then we compare indices

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_index = {}
        map_t_index = {}

        for i in range(len(s)):
            if s[i] not in map_s_index:
                map_s_index[s[i]] = i

            if t[i] not in map_t_index:
                map_t_index[t[i]] = i

            if map_s_index[s[i]] != map_t_index[t[i]]:
                return False

        return True

print(Solution().isIsomorphic("egg", "add"))