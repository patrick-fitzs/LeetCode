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

        # easy method
        #counter_s = Counter(s)
        #counter_t = Counter(t)
        #return counter_s == counter_t

            # or you can do
        countChars = {}

        for letter in s:
            if letter not in countChars:
                countChars[letter] = 1
            else:
                countChars[letter] += 1

        for letter in t:
            if letter in countChars and countChars[letter] > 0:
                countChars[letter] -= 1

            else:
                return False

        return True


print(Solution().isAnagram("anagram", "nagaram"))


